FROM golang:1.26-alpine AS builder

WORKDIR /src

COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o /worker .

FROM alpine:3.20

RUN adduser -D -H -u 10001 appuser
USER appuser

COPY --from=builder /worker /worker

ENTRYPOINT ["/worker"]
