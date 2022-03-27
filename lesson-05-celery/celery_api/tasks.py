from .worker import app
from celery.utils.log import get_task_logger
import time

# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)

@app.task(name='celery_api.run_script')
def run_script(client_name):
    celery_log.info(f"Starting run_script...")
    for i in range(2):
        time.sleep(10)
        celery_log.info(f"Hi, {client_name}")
    celery_log.info(f"Celery task completed!")
    return 'OK'