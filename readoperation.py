#!/usr/bin/python
import MySQLdb
# Open database connection
db = MySQLdb.connect("<host>","<user>","<passwd>","<db>")
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)
try:
    # Execute the SQL command and fetch all the rows
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # Now print fetched result
        print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
              (fname, lname, age, sex, income)
except:
    print "Error: unable to fetch data"
# disconnect from server
db.close()

