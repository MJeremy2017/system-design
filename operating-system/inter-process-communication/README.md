# Inter-Process Communication

Two major ways that process talk to each other.

**Shared Memory**

```
A process can create a shared memory space that the other process can access.
```

In general, the process that wants to communicate creates the shared memory region in its own address
space. Other processes that wish to communicate to this process need to attach their address space to this shared memory segment.

![img.png](shared-memory.png)

**Messaging**

```
A process talk to the operating system(kernel) and the other process would receive the message from there.
```

![img.png](messaging.png)

## Pipe

A pipe is used in the case of communication using messages. A pipe is a connection between two or more processes.