# Locust Performance Test Report

## Test Object

Task Manager API built with FastAPI.

## Scenario

Mixed workload scenario:

- GET /tasks
- GET /tasks/{id}
- POST /tasks
- PUT /tasks/{id}
- DELETE /tasks/{id}

## Load Profile

- Users: 100
- Spawn rate: 10 users/second
- Host: http://127.0.0.1:8000

## Metrics Observed

- Average response time
- 95th percentile response time
- Requests per second
- Failure rate

## Result Summary

The API handled the mixed workload scenario with stable response times and no critical failures during the test run.

## Tools

- Locust
- FastAPI
- SQLite