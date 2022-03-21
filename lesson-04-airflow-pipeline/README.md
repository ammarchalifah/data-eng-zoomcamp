# Learning Notes

OS: Windows 11

## Step-by-step
1. Ensure you put the Google security key (JSON) inside `.google/credentials`. Create Airflow basic directories as well (`/dags`, `/logs`, and `/plugins`).
2. Build the image (might take a long time)
```
docker-compose build
```
3. Initialize Airflow
```
docker-compose up airflow-init
```
4. Start the containers
```
docker-compose up -d
```

***

## Airflow
1. Lalala

## Google Cloud Storage (Data Lake)
1. It is possible to transfer object betweek cloud storages (GCS, AWS S3, Azure Blob, etc) using Transfer Service. Wow cool.

## Google BigQuery (Data Warehouse & Data Mart)
1. Create partition and cluster for efficiency.