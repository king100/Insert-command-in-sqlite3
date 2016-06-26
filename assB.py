# Assignment 3b -prompt the user


# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("newnum.db")

# create the a cursor object used to execute SQL commands
cursor = conn.cursor()

prompt = """
Select the operation that you want to perform [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""

# loop untill user enters a valid operation number[1-5]
while True:
   # get user input
   x = raw_input (prompt)

   # if user enters any choice from from 1-4
   if x in set (["1","2","3","4"]):
      # parse the corresponding operation = {1: "avg", 2:"max", 3: "min", 4: "sum"}[int(x)]

      # retrieve data
      cursor.execute("SELECT {}(num) from numbers".format(operation))

      # fetchone() retrieves one record from the query
      get = cursor.fetchone()

      # output result to screen
      print operation + ": %f"  % get [0]

# if user enters 5
if x == "5":
   print "Exit"

   


