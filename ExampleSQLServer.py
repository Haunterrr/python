import pypyodbc

mySQLServer = "ANSIL\SQLEXPRESS"
myDatabase = "northwind"

connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=' + mySQLServer + ';'
                              'Database=' + myDatabase + ';')

cursor = connection.cursor()

mySQLQuery = ("""
                SELECT CompanyName, ContactName, country
                FROM dbo.Customers
                WHERE country = 'Canada'
               """)

cursor.execute(mySQLQuery)
results = cursor.fetchall()

for row in results:
    companyname = row[0]
    contactname = row[1]
    countryname = row[2]

    print("Welcome :" + str(companyname) + " User: " + str(countactname) + " From: " + str(countryname))

connection.close()
