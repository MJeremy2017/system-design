# Consistency Model

## Strong Consistency
Each read response would always reflect the latest data. But it comes at cost:

- Latency may be higher.
- Strongly consistent reads use more throughput capacity than eventually consistent reads (2 times in `DynamoDB`).


## Eventual Consistency

Each read may not reflect the latest data, but if you wait for a while, the response should return
the latest data.
