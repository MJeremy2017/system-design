# SQL Indexing Mechanism

Create indexing on columns will help to accelerate the searching speed.

- Indexing on a column creates a **sorted data structure**.
- When searching for a particular element, instead of search through linearly `O(N)`, it becomes a binary search
with `O(logN)` complexity.
- Each node in the data structure would store the value of the index and a pointer to the original table so that
it can retrieve other columns.
- [Reference](https://chartio.com/learn/databases/how-does-indexing-work/)