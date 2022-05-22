# Inter-Thread Communication

Take the example in Java.

- **wait()**: This is will release the lock of acquired by the current thread and wait until a. timeout b. notified.
- **notify()**: Notify the first thread that is accessing the object. This does not release the lock until the current
thread is finished running.
- **notifyAll()**: Notify all threads that are accessing the same object.
