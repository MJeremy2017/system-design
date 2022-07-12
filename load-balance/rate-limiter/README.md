# Algorithms

## Token Bucket

Two key parameters are required:

- **Bucket size**: The maximum number of tokens allowed in the bucket.
- **Refill rate**: Refill rate.

A bucket will be initialised with a fixed size, and periodically, a fixed number of tokens would be refilled
into bucket, and each request would take one token, and when tokens are all taken, the request would be dropped.


![img.png](token-bucket.png)

In this example, the token bucket size is 4, and the refill rate is 4 per 1 minute.

![img.png](tb2.png)


## Leaky Bucket

Normally implemented with a FIFO queue. And requests are processed at a fixed rate, when the queue is full, new requests are dropped.

- When a request arrives, the system checks if the queue is full. If it is not full, the request is added to the queue.
- Otherwise, the request is dropped.
- Requests are pulled from the queue and processed at regular intervals.

![img.png](leaky-bucket.png)

**Pros:**

- Memory efficient given the limited queue size.
- Requests are processed at a fixed rate therefore **it is suitable for use cases that a stable outflow rate is needed**.

**Cons:**

- A burst of traffic fills up the queue with old requests, and if they are not processed in time, recent requests will be rate limited.
- There are two parameters in the algorithm. It might not be easy to tune them properly.

## Fixed Window Counter

It divides the time into fixed window size, where in each slot there allows only fixed number of requests.

![img.png](fixed-window.png)

Major drawback is at the edges of the window, there could be more requests than allowed quota.

## Sliding Window

It keeps track of the request timestamp and keeps counting the number of requests in the log.

For example, suppose the rate limit is `2 reqs/min`, when a new reqeust `(req_a, t)` comes in, it will be inserted
into the log, and it will count the number of requests in `[t-60s, t]`, if it exceeds `2`, the request will
be denied, otherwise will be processed.


**Pros:**
- Rate limiting implemented by this algorithm is **very accurate**. In any rolling window, requests will not exceed the rate limit.

**Cons:**
- The algorithm **consumes a lot of memory** because even if a request is rejected, its timestamp might still be stored in memory.

