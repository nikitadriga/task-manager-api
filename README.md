# Task Manager API (FastAPI + Testing + Performance)

## Overview

This project is a REST API built with FastAPI for managing tasks.  
It demonstrates backend development, automated testing, and performance testing.

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pytest
- Locust
- Apache JMeter

## API Endpoints

| Method | Endpoint        | Description       |
|--------|----------------|------------------|
| POST   | /tasks         | Create task       |
| GET    | /tasks         | Get all tasks     |
| GET    | /tasks/{id}    | Get task by ID    |
| PUT    | /tasks/{id}    | Update task       |
| DELETE | /tasks/{id}    | Delete task       |

## Running the Project

uvicorn app.main:app --reload

Swagger UI:
http://127.0.0.1:8000/docs

## Testing

Run tests:
pytest -v

Test coverage includes:
- Create
- Read
- Update
- Delete
- Error handling (404)

## Performance Testing

Locust:
- Simulated concurrent users
- Mixed workload (GET, POST, PUT, DELETE)
- Randomized data
- Dynamic task ID handling

JMeter:
- Load testing with concurrent users
- Multiple API endpoints tested
- Response time and throughput analysis

## Key Findings

- API functions correctly under normal load
- Response time increases under high load
- SQLite causes locking under concurrent write operations
- POST requests may fail under heavy concurrency

## Limitations

- SQLite is not suitable for high concurrency
- No indexing or query optimization
- No production-grade database

## Possible Improvements

- Switch to PostgreSQL
- Add indexing
- Optimize queries
- Add authentication
- Containerize with Docker

## Author

Mykyta Driha