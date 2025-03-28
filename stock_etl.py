from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from datetime import datetime, timedelta
import requests
import pandas as pd
from google.cloud import storage

# Set Default Args
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define API function
def fetch_stock_data():
    api_url = "https://api.polygon.io/v2/aggs/ticker/AAPL/prev?apiKey=YOUR_API_KEY"
    response = requests.get(api_url)
    data = response.json()
    
    df = pd.DataFrame(data['results'])
    df.to_csv('/tmp/stock_data.csv', index=False)

# Upload data to Google Cloud Storage
def upload_to_gcs():
    storage_client = storage.Client()
    bucket = storage_client.bucket("your-gcs-bucket-name")
    blob = bucket.blob("stock_data/stock_data.csv")
    blob.upload_from_filename("/tmp/stock_data.csv")

# Define DAG
dag = DAG(
    'stock_market_etl',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
)

# Tasks
fetch_task = PythonOperator(
    task_id='fetch_stock_data',
    python_callable=fetch_stock_data,
    dag=dag
)

upload_task = PythonOperator(
    task_id='upload_to_gcs',
    python_callable=upload_to_gcs,
    dag=dag
)

load_to_bigquery = BigQueryInsertJobOperator(
    task_id="load_to_bigquery",
    configuration={
        "query": {
            "query": """
                CREATE OR REPLACE TABLE `your_project.your_dataset.stock_data` AS
                SELECT * FROM `your-gcs-bucket-name.stock_data.stock_data.csv`
            """,
            "useLegacySql": False,
        }
    },
    dag=dag,
)

# DAG Execution Order
fetch_task >> upload_task >> load_to_bigquery
