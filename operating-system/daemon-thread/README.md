# Daemon Thread vs. User Thread

- Daemon threads are low priority threads that always run in the background while user threads run in the foreground.
- When all the user threads have finished their tasks, the program would shut down daemon threads.
- Daemon threads are harder to get resources compare to user threads.
- Daemon threads are not used for critical tasks.

