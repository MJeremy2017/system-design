# Layer 4  vs. Layer 7 Load Balancing

## Layer 4 Load Balancing

Layer 4 Load Balancing operates on transport layer which has no knowledge of the content. It simply receives and
deliver the packets. As a matter of fact, it is generally faster. On the contrary, it is unable to do
content-aware load balancing or do any decryption.

## Layer 7 Load Balancing
As opposed to Layer 4 Load Balancing, Layer 7 load balancing operates on application layer and is content-aware.
A layer 7 load balancer terminates network traffic, performs decryption as needed, inspects messages, makes content-based routing decisions
