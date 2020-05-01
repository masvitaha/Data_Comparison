import pyodbc


class MSSQLConnector():
    servername = input("Enter the MS SQL servername : ")
    databasename = input("Enter the MS SQL Database name : ")
    try:
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                              'Server=' + servername + ';'''
                                                       'Database=' + databasename + ';'''
                                                                                    'Trusted_Connection=yes;')

    except pyodbc.Error as err:
        print(err)
        exit(0)
