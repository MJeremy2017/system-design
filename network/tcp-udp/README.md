# TCP and UDP

## Transmission control protocol (TCP)

TCP is a connection-oriented protocol over an **IP network**. 
Connection is established and terminated using a handshake. 
_**All packets sent are guaranteed to reach the destination in the original order and without corruption through**_:

- Sequence numbers and checksum fields for each packet
- Acknowledgement packets and automatic retransmission

If the sender does not receive a correct response, it will resend the packets. If there are multiple timeouts, the connection is dropped. 
TCP also implements flow control and congestion control. These guarantees cause delays and generally result in less efficient transmission than UDP.

To ensure high throughput, web servers can keep a large number of TCP connections open, resulting in high memory usage. 
It can be expensive to have a large number of open connections between web server threads and say, a memcached server. 
Connection pooling can help in addition to switching to UDP where applicable.

TCP is useful for applications that require high reliability but are less time critical. Some examples include web servers, database info, SMTP, FTP, and SSH.

**Use TCP over UDP when:**

- You need all of the data to arrive intact
- You want to automatically make a best estimate use of the network throughput


## User datagram protocol (UDP)

UDP is **connectionless**. Datagrams (analogous to packets) are guaranteed only at the datagram level. 
Datagrams might reach their destination **_out of order or not at all_**. 
UDP does not support congestion control. Without the guarantees that TCP support, UDP is generally more efficient.

UDP can broadcast, sending datagrams **to all devices on the subnet**.

UDP is less reliable but works well in real time use cases such as VoIP, video chat, streaming, and realtime multiplayer games.

**Use UDP over TCP when**:

- You need the lowest latency
- Late data is worse than loss of data
- You want to implement your own error correction