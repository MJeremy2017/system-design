# Mutex vs. Semaphore

## Mutex

Mutual exclusive object controls multiple threads accessing the same resource. At each point of time, there is 
only one thread can **acquire** the lock and access the resource, lock will be **released** after use.


## Semaphore

Semaphore is an integer variable that count the available resource for process synchronization. It uses
**wait()** and **signal()** function to control the variable and at each time only on process can change the variable.

For example, given 4 available resources, if one
process or thread takes the resource, the count would become 3. And when the count become 0, no new process can use the
resource until other **signal** done.

A binary semaphore controls one resource and the variable is either 0 or 1. It can achieve the effect of mutex, but
it is NOT mutex.


## Difference between Mutex and Semaphore

- Mutex uses a locking mechanism i.e. if a process wants to use a resource then it locks the resource, 
uses it and then release it. But on the other hand, semaphore uses a signalling mechanism where wait() and signal() 
methods are used to show if a process is releasing a resource or taking a resource.
- A mutex is an object but semaphore is an integer variable.
- In semaphore, we have wait() and signal() functions. But in mutex, there is no such function.
- A mutex object allows multiple process threads to access a single shared resource but only one at a time. 
On the other hand, semaphore allows multiple process threads to access the finite instance of the resource until available.
- In mutex, the lock can be acquired and released by the same process at a time. 
But the value of the semaphore variable can be modified by any process that needs some resource but only one process 
can change the value at a time.