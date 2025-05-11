import sqlite3
import csv

dbConnection = sqlite3.connect("myDatabase.db")
dbCursor = dbConnection.cursor()

#create three tables for Employees, Pay and social security
try:
    sCreateTable = "CREATE TABLE Employee(EmployeeID int, Name text)"
    dbConnection.execute(sCreateTable)
    print(sCreateTable)

    sCreateTable = "CREATE TABLE Pay(EmployeeID int, year int, Earnings real)"
    dbConnection.execute(sCreateTable)
    print(sCreateTable)

    sCreateTable = "CREATE TABLE SocialSecurityMinimum(Year int, Minimum real)"
    dbConnection.execute(sCreateTable)
    print(sCreateTable)

    dbConnection.commit()

except sqlite3.OperationalError: print("Could not create table")

#pay.txt
sInsertPay = "INSERT INTO Pay(EmployeeID, year, Earnings) VALUES("
sInsertPayReset = sInsertPay

with open("Pay.txt", "r") as file:

    iRows = 0

    reader = csv.reader(file)

    next(reader)

    for row in reader:
        #print(row)

        sInsertPay += f"{row[0]}, {row[1]}, {row[2]})"
        print(sInsertPay)

        #execute insert

        try:
            dbConnection.execute(sInsertPay)
            iRows += 1

        except sqlite3.OperationalError:
            print("Could not insert")

        sInsertPay = sInsertPayReset

    dbConnection.commit()
    print(f"Rows Loaded: {iRows}")
sdfsdfdsdfs
#SocialSecurityMinimum.txt
sInsertSocialSecurityMinimum = "INSERT INTO SocialSecurityMinimum(Year, Minimum) VALUES("
sInsertSocialSecurityMinimumReset = sInsertSocialSecurityMinimum
#headerList = []
#dataList = []

with open("SocialSecurityMinimum.txt", "r") as file:

    iRows = 0

    reader = csv.reader(file)

    next(reader)

    for row in reader:
        #print(row)

        sInsertSocialSecurityMinimum += f"{row[0]}, {row[1]})"
        print(sInsertSocialSecurityMinimum)

        #execute insert
        try:
            dbConnection.execute(sInsertSocialSecurityMinimum)
            iRows += 1

        except sqlite3.OperationalError: print("Could not insert")

        sInsertSocialSecurityMinimum = sInsertSocialSecurityMinimumReset

    dbConnection.commit()
    print(f"Rows Loaded: {iRows}")

#Employee.txt
sInsertEmployee = "INSERT INTO Employee(EmployeeID, Name) VALUES("
sInsertEmployeeReset = sInsertEmployee
#headerList = []
#dataList = []

with open("Employee.txt", "r") as file:

    iRows = 0

    reader = csv.reader(file)

    next(reader)

    for row in reader:
        #print(row)

        sInsertEmployee += f"{row[0]}, '{row[1]}')"
        print(sInsertEmployee)

        #execute insert
        try:
            dbConnection.execute(sInsertEmployee)
            iRows += 1

        except sqlite3.OperationalError: print("Could not insert")

        sInsertEmployee = sInsertEmployeeReset

    dbConnection.commit()
    print(f"Rows Loaded: {iRows}")

#join and make a report
dbCursor.execute("""
    SELECT a.Name, b.Year, b.Earnings, c.Minimum
    FROM Employee AS a
    JOIN Pay AS b ON a.EmployeeID = b.EmployeeID
    JOIN SocialSecurityMinimum AS c ON b.Year = c.Year;
""")

#print("Employee Name, Year, Earnings, Minimum, Include")
print(f"{'Employee Name':<20} {'Year':<5} {'Earnings':>15} {'Minimum':>15} {'Include':>10}")
for row in dbCursor.fetchall():

    fResult = ""

    if row[2] >= row[-1]: fResult = "Yes"

    else: fResult = "No"
    print(f"{row[0]:<20} {row[1]:<5} {row[2]:>15,.2f} {row[3]:>15,.2f} {fResult:>10}")
