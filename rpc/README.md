# REST
Client acts on a set of resources defined and managed by server. **All communications are stateless and cacheable.**

Being stateless, REST is great for horizontal scaling and partitioning.

# RPC

As a predecessor of REST, RPC (Remote Procedure Call) is a software architecture dating back to the 1970s. 
It allows client to invoke a function on the remote server and get a response.

However, comparing to REST, the RPC invoke function are put in the URI,
- RPC: An RPC API request might use POST `/deleteResource` and have a query string that says `{ “id”: 3 }`  
- REST: A REST API request would write this request as DELETE `/resource/2`

# gRPC

Some key difference from `REST`.

## Use Protobuf vs. Json

- Protobuf is highly compressed and focus on serialization and de-serialization.
- Conversely, Protobuf is less human-readable.
- Protobuf transmission is faster than json.

## Built on HTTP2 vs. HTTP1

- Http1 serves each request separately and each connection is short-lived (closes after a request is done).
- Http2 can serve a stream of request reusing the same connection.

## In Born Code Generation Tools.

- gRPC has built-in code generation that is able to build code of various languages, which, is especially 
important in modern architecture with various microservices written in different languages.

## Faster

- gRPC is generally 7 times faster in receiving data and 10 times faster in sending data against REST.