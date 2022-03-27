from celery import Celery

app = Celery(
    'celery_web',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/1',
    include=['celery_api.tasks']
)