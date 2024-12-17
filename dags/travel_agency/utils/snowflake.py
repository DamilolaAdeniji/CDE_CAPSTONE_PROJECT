import snowflake.connector
from dotenv import load_dotenv
import os
load_dotenv()

import pandas as pd

conn = snowflake.connector.connect(
    user=str(os.environ['user']),
    password=str(os.environ['password']),
    account=str(os.environ['account']),
    warehouse=str(os.environ['warehouse']),
    database=str(os.environ['database']),
    schema= str(os.environ['schema'])
    )


def snowflake_reader(query):
    return pd.DataFrame(conn.cursor().execute(query))