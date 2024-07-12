# My NoSQL Database

A simple NoSQL database using SQLite as the underlying storage engine.

## Installation

To install the package, run the following command:

pip install my-nosql-database


## Usage

To use the package, import the `NoSqlite` class and create a `Table` instance for the table you want to use. Here's an example:

```python
from my_nosql_database import NoSqlite

# Create a new database instance
db = NoSqlite("my_database.db")

# Create a new table instance for the "users" table
users = db.table("users")

# Fetch all data from the "users" table
print(users.fetch())

# Fetch data from the "users" table where the name is "Bob Johnson"
print(users.fetch({"name": "Bob Johnson"}))
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.