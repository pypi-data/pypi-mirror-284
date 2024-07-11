# SQL Sanity Check

A Python Library to help perform tests on SQL engines to assess the quality of the data.

Created by Jose Santos
[josemrsantos@gmail.com](mailto:josemrsantos@gmail.com)
[https://www.linkedin.com/in/josemrsantos/](https://www.linkedin.com/in/josemrsantos/)

## How it works

It could not be more simple: Create SQL code that returns rows if you want the test to fail.

### A more intuitive way to look at these SQL tests

A bit more information is probably needed, because "return rows if you want the test to fail", sounds a bit counter-intuitive. To make a bit more "intuitive", imagine that you have a table (**TableA**) that is the source, then you need to make a Transformation (**T1**) that outputs into the destination table (**TableB**). Given that **T1** might become quite complex, we want to make sure every time an update happens to **TableA** , that gets refletcted in **TableB**. A "simple test" would be to check if **TableB** has the same ids as **TableA** (for the sake of keeping it simple, we are assuming that **T1** transfers a column **TrackId** from **TableA** to **TableB** as is). The test could look something like this:

```
SELECT ta.TrackIdasmissing_id
FROM TableA ta
LEFT JOIN TableB tb ON ta.TrackId=tb.TrackId
WHERE tb.TrackId IS NULL;
```

*These 2 tables actually exist in the demo DB Chinook.db and are both created from the table **Track**. A SQK test case with that exact code is also included in the sql_tests directory.*

### Some Details

You create individual SQL queries that you place in .sql files, inside a directory (look at the sql_tests directory for a few examples).

The library will run all SQL files inside the specified directory, and will fail with an exception if any of the tests fail. The name of the file, its contents and the values returned are also given to the output_objects.

A default output_object is already included that only outputs to stdout (any log call) or to stderr (any error call)

### Anatomy of a connector

A connector is an idependent Python module that takes care of the connection to a specific SQL DB engine.
The Class created needs to be a context manager so that it can be used with the with statement. In the Library this class will be called something like:

```python

with self.connector as conn:
    result = conn.execute_query(sql_code)
```

The following methods should be implemented to the class:

* **connect**: Method that creates a connection to the DB
* **execute_query**: Method that send a SQL command to the server and returns the result as an iterator
* **close**: Method that closes a connection to the DB
* `__enter__` and `__exit__`: So that the class is a content manager.

  Looking at the module connector_sqlite.py might also help.
* ## SQL tests code examples

### Simple tests

A few simple tests have already been included in the sql_tests directory and these work around chacking different values on different tables. Counting the number of lines might also be a simple and effective test. eg:

```sql
WITH table_track AS (SELECT count(*) AS count_t FROM Track),
     table_invoiceline AS (SELECT count(DISTINCT TrackId) AS count_il FROM InvoiceLine)
SELECT count_t, count_il
FROM table_track, table_invoiceline
WHERE count_t < count_il;
```

The previous test only checks if we don't have more distinct TrackIds on the table **InvoiceLine** than the number of actual Tracks in tha table **Track**.

### Tests on foreign data

This is very specific and it is more related with good writting good SQL. Several DB servers are offering some sort of "foreign data access". A few examples are the FDW on PostgreSQL that allows one PostgreSQL server to have access to tables that are on a different server. The main caveat of this, is that any query that is done on the server that only has the "foreign table" that itself is in a second server, the actual query will be done on the "second server".

An example:

**ServerA** has 2 tables: **table_a_1** and **table_a_2**. **ServerB** has only 1 table: **table_b_1**, but it also has a FDW connection to ServerA, so it also "allows queries" on those tables.

If we do a SELECT on **ServerB** such as `SELECT name FROM table_a_1 LIMIT 10`, that query will run on **ServerA** and return the result (using the network) to **serverB**. This is not a problem, because it is all running on the same server (in this case **ServerA**) and the volume of data going throught the network is not very large. This is just a simple example, but Redshift also has some similar capabilities as well as other capabilities, where this is not an issue. If you use any sort of "data sharing", please check the DB server that you are using. if this might something you need to consider.

When we have a case where we make a query to ServerB that might send a part or all the query to ServerA, the general advice would be to keep it as seperate as possible and minimise possible network usage.

A good example of keeping to these rules, has already been given before. Lets say that we have **Track** and **InvoiceLine** on different servers. Using CTEs and fetching a low number of rows/data is a good way to create a SQL test (please see the previous code example).

## Usage and contributions

The code (as simple as it is), is released under the MIT license, that AFAIK is one of the most (if not the most) permissive license. So, please use it as you wish and get in touch if you need anything, but don't blame me if something goes wrong.

In terms of contributions, I would be very happy to accept anything you can contribute with. From small fixes to this Readme to adding other connectors that could help others.
