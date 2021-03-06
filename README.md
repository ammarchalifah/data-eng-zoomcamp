# Data Engineering Zoomcamp Learning Notes

DataTalks hosted a series of webinar videos for a data engineering bootcamp (or in their term: zoomcamp), and I decided that I want to join it! In this repository, I tried to replicate the projects presented by the instructor. Disclaimer, I often times use the code from the official zoomcamp repository (https://github.com/DataTalksClub/data-engineering-zoomcamp).

I partitioned the materials into lessons, and each lesson contained a project and a learning note (`README.md`). This notes contains the information to reproduce the works and some general insights that I got from the project.

This repository is not designed for public use, hence the learning notes are not well-structured and kinda random. I only put notes on the thing that feels new to me. So, please refer to the official repository for more detailed notes. Enjoy! :D

## Contents
**Lesson 1 - Data Ingestion (CSV to Postgres)**

Ingest data from CSV in host machine into Postgres database in a Docker container. Connect Postgres container with a PgAdmin (inside a container) through docker network.

**Lesson 2 - Terraform & GCP**

Using Terraform to manage Google Cloud infrastructures.

**Lesson 3 - GCP VM Exploration**

Using SSH to access GCP VM instance. Remote access exploration via SSH.

**Lesson 4 - Airflow, GCS, and BigQuery**

Orchestrate workflows using Airflow, ingest data to Google Cloud Storage, and create data warehouse using BigQuery.

**Lesson 5 - Celery**

Create an API endpoint using FastAPI, task queue manager using Celery, task monitoring using Flower, and message broker using RabbitMQ.

**Lesson 6 - DBT**

Data catalog, documentation, and lineage using DBT (Data Build Tool).

**Lesson 7 - Kafka**

Real-time data streaming, broker-producer-consumer, and topic subscription.