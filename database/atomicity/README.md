# Atomicity

```
Atomicity is a feature of databases systems dictating where a transaction must be all-or-nothing. That is, 
the transaction must either fully happen, or not happen at all. It must not complete partially.
```


Atomicity is achieved in database by using transaction logging. When a transaction happens, its before-state
is recorded, and the records of that transaction in the database is locked until it is either committed or rolled back.

```
At the end of the transaction, 
   |_ if committing, you simply write a record into the log saying you committed and release the locks. 
   |_ if you roll back, you need to walk back through the transaction log undoing all your changes.
        (so each change written to the log file contains a "before image" of how the data looked originally)
```
