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
