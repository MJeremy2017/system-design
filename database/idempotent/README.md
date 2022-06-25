# Idempotent

Idempotent is an operation that no matter how many times you execute it, the result would come out the same.
For example, in math, `abs` is an idempotent operation.

In database, for example, with an idempotent delete function, if a request to delete a file is successfully completed 
for one program, all subsequent requests to delete that file from other programs would return the same success confirmation message.
In a non-idempotent delete function, an error would be returned for the second and subsequent requests indicating that the file was not there.

## How to make a transaction that modifies data idempotent?

If a transaction changes the data and during the transaction the worker failed and the state of the transaction
would become unknown. To make retry of the same transaction to be idempotent, client side can initiate a `idempotent key`,
a unique token that marks a transaction, so if the previous transaction with the same key has succeeded, it will not
execute the transaction again, otherwise it would redo the transaction, thus achieving exactly once operation.

## Exact Once in Kafka

Same as the logic above, for each event, kafka would assign a sequence key to the event which is 
persisted to the broker log (this sequence number is persisted to the replicated log, so even if the leader fails, 
any broker that takes over will also know if a resent is a duplicate). 

In case of the system fails, the same message with the same sequence key would not be sent again.
