# Polling

Client periodically asks the server whether there is new messages.

![img.png](poll.png)

# Long Polling

_Making repeated requests to a server wastes resources, as each new incoming connection must be established, 
the HTTP headers must be parsed, a query for new data must be performed, and a response (usually with no new data to offer) must be generated and delivered. 
The connection must then be closed, and any resources cleaned up._ 

In long polling, server would hold the connection until either there is a new message comes in or timeout.

![img.png](long-poll.png)

Difference on the client side, with basic polling, the client would normally leave a small periodic window before calling
the server again once response received in order to reduce the load on the server. But in long polling, the client can
initiate the connection immediately upon a response is received.
