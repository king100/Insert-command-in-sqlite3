# INSERT Command with Error Handler


# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object usde to execute SQL commands
cursor = conn.cursor()

try:
   # insert data
   cursor .execute("INSERT INTO populations VALUES('New york City', 'NY', 8200000)")
   cursor .execute("INSERT INTO populations VALUES('San Francisco', 'CA', 800000)")
   # commit the changes
   conn.commit()
except sqlite3.OperationalError:
   print "Oops! something went wrong. Try again ..."
# close the databese connection
conn.close
