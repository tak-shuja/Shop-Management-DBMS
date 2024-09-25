import os
import mysql.connector
from dotenv import load_dotenv

# load the .env variables
load_dotenv()

# get the required variables from .env file
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

# create a db connection object
try:
    db_conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
    )
    print(f"Connected to database: {DB_NAME}")
except mysql.connector.Error as err:
    print(f"Error: {err.msg}")
    exit(1)

cursor = db_conn.cursor()

# get the db auth variables from the .env file
ADMIN_UNAME = os.getenv('ADMIN_AUTH_UNAME')
ADMIN_PASS = os.getenv('ADMIN_AUTH_PASS')

if not ADMIN_UNAME or not ADMIN_PASS:
    print("Please set the admin auth and pass values as ADMIN_AUTH_UNAME and ADMIN_AUTH_PASS respectively in the .env file.")
    exit(1)

# Create customers table query
customers_table_query = """
CREATE TABLE IF NOT EXISTS customers (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    address VARCHAR(40) NOT NULL,
    paid DECIMAL(10, 2) NOT NULL,
    remaining DECIMAL(10, 2) NOT NULL,
    time TIME,
    date VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
);
"""


# Create authentication table query
auth_table_query = """
CREATE TABLE IF NOT EXISTS authentication (
    name VARCHAR(20) NOT NULL,
    password VARCHAR(25) NOT NULL
);
"""

# Insert admin credentials query
auth_entry_query = """
INSERT INTO authentication (name, password)
VALUES (%s, %s)
ON DUPLICATE KEY UPDATE password = VALUES(password);
"""

# Execute the SQL queries
try:
    cursor.execute(customers_table_query)
    cursor.execute(auth_table_query)

    # Check if the admin already exists (prevents duplicate inserts)
    cursor.execute("SELECT * FROM authentication WHERE name = %s", (ADMIN_UNAME,))
    result = cursor.fetchone()

    if result:
        print("Admin credentials already exist, updating password...")
        cursor.execute("UPDATE authentication SET password = %s WHERE name = %s", (ADMIN_PASS, ADMIN_UNAME))
    else:
        cursor.execute(auth_entry_query, (ADMIN_UNAME, ADMIN_PASS))

    # Commit the changes
    db_conn.commit()
    print("Tables created and admin credentials set/updated.")

except mysql.connector.Error as e:
    print(f"Error: {e.msg}")
    exit(1)
# finally:
    # cursor.close()
    # db_conn.close()
    # print("Database connection closed.")
