# Learning Notes

OS: Windows 11

## Step-by-step
1. Install the Python dependencies
```
pip install -r requirements.txt
```
2. Start FastAPI endpoint
```
uvicorn endpoint:app --reload
```
3. Start Celery worker
```
celery -A celery_api.worker worker --loglevel=INFO
```
4. Start Celery flower to monitor Celery
```
celery flower -A celery_api.worker --broker:pyamqp://guest@localhost
```
5. The current codebase is not working because I haven't set up a broker. Need to get back to this.

***

## Celery
1. Distributed task queue.
2. Needs a message broker in order to work. I want to try Redis or RabbitMQ but haven't tried both of them.

## Flower
1. Celery monitoring tool.

## FastAPI
1. Python package for high performance web API.
2. Automatically create docs page with Swagger UI.