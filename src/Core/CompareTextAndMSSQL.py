import datacompy
import pandas as pd
from pandas import DataFrame

from src.Connection import MSSQL, Text


class CompareData():
    SQL_Query: DataFrame = pd.read_sql_query(
        '''SELECT [Id],[Data]
          FROM [Test]''', MSSQL.MSSQLConnector.conn)

    df = pd.DataFrame(SQL_Query, columns=['Id', 'Data'])

    df1 = pd.read_csv(Text.TxtFileConnector.textfile)

    compare = datacompy.Compare(
        df, df1,
        join_columns='ID',  # You can also specify a list of columns eg ['policyID','statecode']
        abs_tol=0,  # Optional, defaults to 0
        rel_tol=0,  # Optional, defaults to 0
        df1_name='Original',  # Optional, defaults to 'df1'
        df2_name='New'  # Optional, defaults to 'df2'
    )
    print(compare.report())
