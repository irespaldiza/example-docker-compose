# Docker Compose & Swarm Demo Project

Overview

This project demonstrates a realistic multi-service application using Docker Compose. It includes synchronous and asynchronous components, multiple networks, persistent storage, and a reverse proxy.

The goal is to provide a clear and practical example of how services interact in a distributed system, serving as a foundation for understanding container orchestration.

⸻

## Architecture

The system is composed of the following components:
• Proxy (Nginx): Entry point for all HTTP traffic
• Frontend (Nginx static): User interface
• API (Python Flask): Handles requests and business logic
• Worker (Go): Processes jobs asynchronously
• PostgreSQL: Persistent data storage
• Redis: Queue and caching layer

## Flow

    1.	The user accesses the application through the proxy
    2.	The frontend sends requests to the API
    3.	The API stores data in PostgreSQL
    4.	The API pushes jobs to Redis
    5.	The worker consumes jobs from Redis and processes them
    6.	The worker updates the database

⸻

## Network Design

The application is split across three networks:
• public: Exposed services (proxy, frontend)
• backend: Internal communication between proxy, frontend, and API
• data: Data layer (API, worker, PostgreSQL, Redis)

This design illustrates service isolation and controlled communication between components.

⸻

## Project Structure

```yaml
project/
docker-compose.yml

proxy/
nginx.conf

frontend/
index.html

api/
Dockerfile
requirements.txt
app.py

worker/
Dockerfile
go.mod
main.go

db/
init.sql
```

## Requirements

    •	Docker
    •	Docker Compose (v2)

⸻

## Running the Project

### Build and start all services:

```shell
docker compose up --build
```

Access the application at:

```shell
http://localhost:8080
```

## Expected Behavior

    •	Orders can be created through the UI
    •	Data is stored in PostgreSQL
    •	Jobs are queued in Redis
    •	The worker processes jobs asynchronously
    •	Order status transitions:
    •	pending → processing → processed

To monitor background processing:

```shell
docker compose logs worker -f
```

## Useful Commands

Check running services:

```shell
docker compose ps
```

View logs:

```shell
docker compose logs
```

Recreate the environment from scratch:

```shell
docker compose down -v
docker compose up --build
```

## Key Concepts Demonstrated

    •	Multi-service applications with Docker Compose
    •	Service discovery via container names
    •	Network segmentation
    •	Persistent storage with volumes
    •	Reverse proxy patterns
    •	Asynchronous processing using a queue and worker
    •	Multi-stage builds with Go
    •	Clear separation of responsibilities across services

## Next Step: Docker Swarm

Next Step: Docker Swarm

This same application can be deployed using Docker Swarm.

Key concepts to explore in that context include service replication, desired state management, and built-in load balancing.

| Notes
| This project is designed to be simple enough for learning purposes while still reflecting real-world architectural patterns.
