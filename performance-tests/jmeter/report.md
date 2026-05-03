# JMeter Performance Test

## Test Setup

- Tool: Apache JMeter
- Users: 50
- Ramp-up: 10 seconds
- Loop count: 10

## Endpoints Tested

- GET /tasks
- POST /tasks
- GET /tasks/{id}

## Results Summary

- Average response time: ~1200 ms
- Throughput: ~10 requests/sec
- Error rate: ~17%

## Observations

- GET requests slow down under load
- POST requests fail under high concurrency
- SQLite causes locking during write operations

## Conclusion

The API performs well under low load but shows limitations under concurrent usage due to database constraints.