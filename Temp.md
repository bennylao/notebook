Testing for sqlite3
creating database
```python
from pathlib import Path
import sqlite3

""" if external libraries are required, pip install them can be run automatically
import sys
import subprocess
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])
"""

# Define the database file name and location
db_file = Path(__file__).parent.joinpath('database.db')
print(str(db_file))

# Connect to the database
connection = sqlite3.connect(db_file)
print("Connected to database successfully")

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Create table
create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                        id integer PRIMARY KEY,
                        task_name STRING NOT NULL,
                        priority integer);
                        """


# Execute the SQL query
cursor.execute(create_tasks_table)

# Commit the changes
connection.commit()

# Insert table data
insert_data1 = """INSERT INTO tasks (id, task_name, priority) VALUES (1, 'task1', 11);"""
insert_data2 = """INSERT INTO tasks (id, task_name, priority) VALUES (2, 'task2', 12);"""
cursor.execute(insert_data1)
cursor.execute(insert_data2)
connection.commit()

# Select data from table
cursor.execute("SELECT * FROM tasks")

# load data into a variable
rows = cursor.fetchall()

# print data
for row in rows:
    print(row)

# close the database connection
connection.close()
```

testing for connecting database

```python
from pathlib import Path
import sqlite3

""" if external libraries are required, pip install them can be run automatically
import sys
import subprocess
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])
"""

# Define the database file name and location
db_file = Path(__file__).parent.joinpath('database.db')
print(str(db_file))

# Connect to the database
connection = sqlite3.connect(db_file)
print("Connected to database successfully")

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Select data from table
cursor.execute("SELECT * FROM tasks")

# load data into a variable
rows = cursor.fetchall()

# print data
for row in rows:
    print(row)

# close the database connection
connection.close()

```