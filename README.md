# ETL-Pipeline-for-Stock-Market-Data-using-Apache-Airflow

We will set up an ETL pipeline using Apache Airflow to extract stock market data from an API, transform it, and load it into Google BigQuery for analysis. The entire project will be set up without using Docker, making it easy to run on Google Cloud Composer (free-tier) or a local Airflow instance.

![ETL-Pipeline-for-Stock-Market-Data-using-Apache-Airflow - visual selection](https://github.com/user-attachments/assets/c90db1fd-7ea5-401e-bc24-fd33f50b5792)



Step 1: Set Up Apache Airflow on Google Cloud (Free-Tier)
We will use Google Cloud Composer to run Airflow without local installation.
Create a GCP Free-Tier Account
Sign up at Google Cloud.
Activate Cloud Composer and BigQuery.
Enable Cloud Storage, BigQuery, and Pub/Sub.
Create a Cloud Composer Environment
Go to GCP Console → Search "Cloud Composer".
Click Create Environment.
Choose Composer 2 (Free-Tier Eligible).
Select Small VM size (to stay within free-tier).
Click Create and wait for it to set up.

Step 2: Create an Airflow DAG for ETL
Extract stock market data from an API.
Transform it into a structured format (CSV).
Load it into Google BigQuery.
1️⃣ Install Required Libraries in Airflow
Once Cloud Composer is ready, install dependencies:
2️⃣ Write the Airflow DAG (ETL Pipeline)
Create a Python script stock_etl.py inside the dags/ folder.

Step 3: Deploy DAG in Cloud Composer
Open Cloud Composer in GCP Console.
Navigate to "DAGs" and click Upload DAG.
Upload the stock_etl.py file.
Start the DAG and monitor execution.

Step 4: Query Data in BigQuery
Open BigQuery Console.
Run this SQL query to view data:
SELECT * FROM `your_project.your_dataset.stock_data`
LIMIT 10;



![ETL-Pipeline-for-Stock-Market-Data-using-Apache-Airflow - visual selection (1)](https://github.com/user-attachments/assets/f7c4e4d7-9e01-46e9-9478-88c6972f0e62)

