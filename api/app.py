import json
import os

import psycopg2
import redis
from flask import Flask, jsonify, request

app = Flask(__name__)

db = psycopg2.connect(
    host=os.environ["DB_HOST"], database="orders", user="user", password="pass"
)

r = redis.Redis(host=os.environ["REDIS_HOST"], port=6379)


@app.route("/orders", methods=["POST"])
def create_order():
    data = request.json
    name = data.get("name")

    cur = db.cursor()
    cur.execute("INSERT INTO orders (name) VALUES (%s) RETURNING id;", (name,))
    order_id = cur.fetchone()[0]
    db.commit()

    # cache
    r.set(f"order:{order_id}", json.dumps({"id": order_id, "name": name}))

    # queue
    r.lpush("jobs", json.dumps({"id": order_id}))

    return jsonify({"id": order_id, "status": "queued"})


@app.route("/orders", methods=["GET"])
def list_orders():
    cur = db.cursor()
    cur.execute("SELECT id, name FROM orders;")
    rows = cur.fetchall()

    return jsonify([{"id": r[0], "name": r[1]} for r in rows])


app.run(host="0.0.0.0", port=5000)
