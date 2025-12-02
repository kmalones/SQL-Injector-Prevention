# SQL-Injection-Reporter

A small Python script that demonstrates the difference between vulnerable SQL string concatenation and secure parameterized queries when accessing a MySQL database. The script runs two simple checks: one using an unsafe concatenated query and one using a parameterized query to show how SQL injection payloads are handled.


## Features
- Demonstrates a vulnerable SQL query (string concatenation).
- Demonstrates a secure parameterized query.
- Runs example payloads and prints whether the injection was successful or blocked.

## Prerequisites
- Python 3.7+
- MySQL server accessible locally or remotely
- Python package: mysql-connector-python

