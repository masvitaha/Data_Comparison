import datacompy
import pandas as pd
from src.Connection import Postgres, MSSQL


class CompareData:
    Postgres.PostgresConnector.cur.execute("SELECT * FROM %s;" % "Test")
    the_data = Postgres.PostgresConnector.cur.fetchall()
    columnNames = [desc[0] for desc in Postgres.PostgresConnector.cur.description]
    the_frame = pd.DataFrame(the_data)
    the_frame.columns = columnNames

    MSSQL.MSSQLConnector()
    SQL_Query = pd.read_sql_query(
        '''SELECT [Id],[Data]
              FROM [Test]''', MSSQL.MSSQLConnector.conn)

    df = pd.DataFrame(SQL_Query, columns=['Id', 'Data'])

    compare = datacompy.Compare(
        df, the_frame,
        join_columns='Id',  # You can also specify a list of columns eg ['policyID','statecode']
        abs_tol=0,  # Optional, defaults to 0
        rel_tol=0,  # Optional, defaults to 0
        df1_name='Original',  # Optional, defaults to 'df1'
        df2_name='New'  # Optional, defaults to 'df2'
    )
    print(compare.report())
