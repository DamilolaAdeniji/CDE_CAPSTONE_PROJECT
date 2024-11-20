from airflow import DAG
#from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from dotenv import load_dotenv
from utils import data_worker,s3_functions
load_dotenv()


default_args = {
    'start_date': datetime(2024, 11, 21),  # Adjust to your schedule
    'retries': 1,
}

api_source = 'https://restcountries.com/v3.1/all'
s3_storage = "s3://dami-cde-bucket/"
raw_destination = "raw/raw_data.parquet"
stage_destination = "stage/staged_data.parquet"


def extract_from_api_to_s3():
    """
    This function takes the raw data from the api endpoint and loads it to the raw_storage within the s3 bucket
    """
    df = s3_functions.export_data_from_api(source=api_source)
    s3_functions.export_df_to_s3(df=df,destination=s3_storage + raw_destination)

def transform_raw_data():
    """
    This function takes the raw data from the raw_destination, transforms it and loads it to a stage_destination
    """
    df = s3_functions.extract_from_s3(path=raw_destination)
    df = data_worker.dataframe_transformer(df)
    s3_functions.export_df_to_s3(df=df,destination=s3_storage + stage_destination)

def load_data_to_dwh():
    pass

with DAG(
    dag_id='travel_agency_dag',
    default_args=default_args,
    description='DAG to load data from restcountries api endpoint to our datawarehouse',
    schedule_interval=None,
) as dag:

    extract_from_api_to_s3 = PythonOperator(
        task_id = "extract_from_api_to_s3",
        python_callable = extract_from_api_to_s3
    )


    transform_raw_data = PythonOperator(
        task_id = "transform_raw_data",
        python_callable = transform_raw_data
    )

extract_from_api_to_s3 >> transform_raw_data