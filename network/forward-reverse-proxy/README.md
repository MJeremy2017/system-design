# Forward/Reverse Proxy

## Forward Proxy
A forward proxy sits in front of a group of **client machines**.

![img.png](forward-proxy-flow.svg)

A will send requests to B, which will then forward the request to C. C will then send a response to B, which will forward the response back to A.

- **To block visits to certain content.**
- **Protect identity** as only the proxy IP is exposed while client IP is hidden.

## Reverse Proxy
A reverse proxy sits in front of a group of **server machines**.

![img.png](reverse-proxy-flow.svg)

All requests from D will go directly to E, and E will send its requests to and receive responses from F. E will then pass along the appropriate responses to D.

- **Load balancing.**
- **Extra security** as the server IP is not exposed.
- **Better performance** as the proxy can also cache content.