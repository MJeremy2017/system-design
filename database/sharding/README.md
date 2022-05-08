# Sharding

Applied in **scaling** issue. Spread data into multiple nodes, each of them store part of the total data.
![img_1.png](../../imgs/sharding.png)

## Sharding Algorithm

- Key-based sharding (hashing).
- Range-based sharding.

# Dynamic/Consistent Hashing

Split data into `virtual nodes`, and each `physical node(machine)` would take a series of `virtual nodes`. 
For each request, we simply find the nearest server to its right, in a clockwise fashion.

![img.png](../../imgs/consistent-hashing.png)

Upon adding new server, at most one other server will be impacted by a change 
in the number of servers.

The example below a new server is added and it maps to index `95`. 
The request that is mapped to index `88` is now served by the new server mapped to index `95`, 
instead of the previous one that was mapped to index `99`.

![img.png](../../imgs/consistent-hashing2.png)
