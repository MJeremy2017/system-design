# SQL Caching Technique

When executing an SQL query, the result is a `ResultSet` that can iterate through. There are multiple caching technique
can be used.

## Store the `ResultSet` as a ByteArray

Here the key would be the query serialised into bytes and value be the serialised `ResultSet`. Thus,
when the same query used again, one can directly get the result that ready to iterate on.

## Extract Partial Fields into Json(Custom Format)

The stored value in cache would be some fields of `ResultSet`. For example, the key
can be a `customer_id`, value `phone, age, ...`, some fields extracted and stored in Json format.

## Extract Partial Fields into Redis built-in Structure

The same case above can be stored in redis `hashmap`, a built-in ready to use structure.

## Extract Partial Fields into Application Structure

The stored structure can also be self-implemented application structure, based on one's custom implementation.
