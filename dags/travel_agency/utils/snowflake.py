import snowflake.connector

import pandas as pd

conn = snowflake.connector.connect(
    user='DFA23DA',
    password='DfestAfrica23',
    account='yprvbzs-ow05669',
    warehouse='DFA23',
    database='dfa23rawdata',
    schema= 'DADATATHON'
    )
conn.cursor().execute("select * from DFA23RAWDATA.dadatathon.growth_stage").fetchall()

def snowflake_reader(query):
    return pd.DataFrame(conn.cursor().execute(query))