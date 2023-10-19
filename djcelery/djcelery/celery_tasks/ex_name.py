import logging

from djcelery.celery_config import app

"""
from djcelery.celery_tasks.ex_name import my_task
my_task.delay()
"""

logging.basicConfig(
    filename="app.log", level=logging.ERROR, format="%(actime)s %(levelname)s %(message)s"
)


@app.task(queue="tasks")
def my_task():
    try:
        raise ConnectionError("Connection Error Occured...")
    except ConnectionError:
        logging.error("Connection error occurred....")
        raise ConnectionError()
