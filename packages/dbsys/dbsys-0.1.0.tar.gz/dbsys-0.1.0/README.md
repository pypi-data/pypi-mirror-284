# dbsys

dbsys is a Python library for managing database operations using SQLAlchemy and pandas. It provides a high-level interface for common database operations, including reading, writing, creating tables, deleting tables, deleting columns, and deleting rows.

## Installation

You can install dbsys using pip:

```
pip install dbsys
```

## Usage

Here's a quick example of how to use dbsys:

```python
from dbsys import manage_db
import pandas as pd

# Create a sample DataFrame
data = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})

# Database URL
db_url = "sqlite:///example.db"

# Create a new table
manage_db(db_url, "my_table", "c", data)

# Read the table
result = manage_db(db_url, "my_table", "r")
print(result)

# Delete a column
manage_db(db_url, "my_table", "dc", column_name="B")

# Delete a row
manage_db(db_url, "my_table", "dr", row_identifier={"A": 2})

# Delete the table
manage_db(db_url, "my_table", "dt")
```

## Features

- Read entire tables
- Write data to tables
- Create new tables
- Delete tables
- Delete specific columns
- Delete specific rows

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
