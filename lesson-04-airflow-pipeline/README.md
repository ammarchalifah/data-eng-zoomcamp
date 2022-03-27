# Learning Notes

OS: Windows 11

## Step-by-step
1. Ensure you put the Google security key (JSON) inside `.google/credentials`. Rename the credential file into `google_credentials.json`. Create Airflow basic directories as well (`/dags`, `/logs`, and `/plugins`).
2. Change the environment variable values in `.env` file, especially for `"_AIRFLOW_WWW_USER_USERNAME"`, `"_AIRFLOW_WWW_USER_PASSWORD"`, `"GCP_PROJECT_ID"`, and `"GCP_GCS_BUCKET"`. Use the project ID and bucket name that you have.
3. Build the image (might take a long time)
```
docker-compose build
```
4. Initialize Airflow
```
docker-compose up airflow-init
```
5. Start the containers
```
docker-compose up -d
```
6. The first DAG (`dag_datalake_taxi`) consists of several tasks, from downloading CSV from a public S3, converting the CSV into a Parquet locally, uploading the file into Google Cloud Storage, and then deleting the unused local CSV and Parquet. The pitfall with this method is there are no validations with the schema (and the corresponding data types for each column). The better approach is to create another function to map input schema into PyArrow schema before writing them down to a Parquet.
7. The second DAG (`dag_dw_trips`) consists of moving the raw Parquet into another GCS directory, then creating an external BigQuery table from those files. Finally, a new BigQuery table also created using a query. This DAG also suffers from missing details, such as creating an Airflow sensor to make this DAG a downstream task for the datalake DAG.

***

## Airflow
1. The complete version uses Celery, Flower, and Redis. Need more effort to understand the connection between those tools.

## Google Cloud Storage (Data Lake)
1. It is possible to transfer object betweek cloud storages (GCS, AWS S3, Azure Blob, etc) using Transfer Service. Wow cool.

## Google BigQuery (Data Warehouse & Data Mart)
1. Create partition and cluster for efficiency.
2. An external BigQuery can be created from a collection of files with the same schema.