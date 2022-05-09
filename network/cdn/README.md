# CDN(Content Delivery Network)

A CDN is a geographically distributed group of servers work together to delivery content faster.
Users will be route to geographically the closest server.

## How does a CDN work?

At its core, a CDN is a network of servers linked together with the goal of delivering content as quickly, cheaply, reliably, and securely as possible. In order to improve speed and connectivity,
a CDN will place servers at the exchange points between different networks.

![img_1.png](cdn.png)

## Push CDN
Proactively update content whenever changes occur on the server.

Sites with a small amount of traffic or sites with content that isn't often updated work well with push CDNs.

## Pull CDN

It update content only when a user request for that particular content(lazily pull), after that the
content will be cached with given TTL.

Sites with heavy traffic work well with pull CDNs, 
as traffic is spread out more evenly with only recently-requested content remaining on the CDN.