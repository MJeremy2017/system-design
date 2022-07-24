# Replication (Availability)

## Master-Slave
Master node would take in both `Read/Write`, while Slave node only accepts `Read`.
- **Only master node can modify the data**.

![img.png](rep1.png)


## Master-Master
All members are responsive to client data queries.
- **all members can modify the data.**

![img_1.png](rep2.png)

### Advantages

- **Availability**: If one master fails, other masters continue to update the database. **Better throughput**.
- **Distributed Access**: Masters can be located in several physical sites, i.e. distributed across the network.

### Disadvantages

- **Consistency**: Most multi-master replication systems are only loosely consistent, i.e. lazy and asynchronous, **violating ACID properties.**
- **Performance**: Eager replication systems are complex and **increase communication latency.**
- **Integrity**: Issues such as conflict resolution can become intractable as the number of nodes involved rises and latency increases.

### Quorum-based voting for replica control

Each of the node that holds a copy would have one vote. Let's say a data item is copied to `V` nodes, so
in total there are `V` votes. And the data item is written to `V_w` nodes and are read from `V_r` node,
the following condition must be satisfied,

- `V_w` + `V_r` > `V`; Ensures strong consistency as at least one node holds the latest data.
- `V_w` > `V/2`.

**Cases**

- If `V_w = 1` and `V_r = V`, then it is optimised for write, as the coordinator only needs to wait for ACK from one node when written.
- If `V_r = 1` and `V_w = V`, then it is optimised for read.

Together with **data versioning**, it ensures at least the latest data can be fetched from at least one node. 
