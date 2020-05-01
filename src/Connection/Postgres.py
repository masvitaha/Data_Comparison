import psycopg2


class PostgresConnector:
    servername = input("Enter the Postgres Servername : ")
    databasename = input("Enter the Postgres Database name : ")
    username = input("Enter the Postgres UserName : ")
    password = input("Enter the Postgres Password : ")
    try:
        conn = psycopg2.connect(host=servername, database=databasename, user=username, password=password)
        cur = conn.cursor()

    except psycopg2.Error as err:
        print(err)
        exit(0)
