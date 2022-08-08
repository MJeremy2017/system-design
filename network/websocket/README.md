# Websocket

The client and the server first establish a connection through HTTP, and then upgrade to websocket connection, 
which is persistent.

![img.png](ws.png)

## Service Discovery

The primary role of service discovery is to recommend the best chat server for a client based on the criteria like 
geographical location, server capacity, etc. Apache Zookeeper is a popular open-source solution 
for service discovery. 
It registers all the available chat servers and picks the best chat server for a client based on predefined criteria.