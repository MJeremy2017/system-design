# SQL Indexing Mechanism

Create indexing on columns will help to accelerate the searching speed.

- Indexing on a column creates a **sorted data structure**.
- When searching for a particular element, instead of search through linearly `O(N)`, it becomes a binary search
with `O(logN)` complexity.
- Each node in the data structure would store the value of the index and a pointer to the original table so that
it can retrieve other columns.
- [Reference](https://chartio.com/learn/databases/how-does-indexing-work/)

```angular2html
CREATE TABLE my_table (
    id int,
    timestamp datatime,
    user_id int,
    name varchar(20),
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES Person(user_id) 
);

CREATE INDEX user_index ON my_table (user_id);
```

Unique index

```angular2html
CREATE UNIQUE INDEX index_name
ON table_name (column1, column2, ...);
```

Composite indexes on column `LastName` and `FirstName`.

```angular2html
CREATE INDEX idx_pname
ON Persons (LastName, FirstName);
```