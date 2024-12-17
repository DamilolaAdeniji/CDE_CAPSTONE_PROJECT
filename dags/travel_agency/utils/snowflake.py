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


def execute_query(query):
    try:
        # Execute the query
        cursor = conn.cursor()
        cursor.execute(query)
        print("Query executed successfully.")

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return "Query executed successfully."
    except Exception as e:
        return f"Error executing query: {e}"
