# Load Balancing Algorithms

There are 2 major types of load balancing algorithm. One is dynamic load balancing and the other is static.

## Dynamic

Dynamic load balancer route based on server resources.
- _Least connection_. Route to server with the least connections, which assumes all server has similar 
capability of handling traffic.
- _Weighted least connection_.
- _Weighted response time_. Route to server with the least response time.
- _Resource-based_. Route based on server CPU, memory etc.

## Static

Static load balancer route based on fixed algorithms.

- _Round-robin._
- _Weighted round-robin._
- _IP address hashing._

