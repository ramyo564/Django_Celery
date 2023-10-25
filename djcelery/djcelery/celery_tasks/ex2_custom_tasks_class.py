import logging

from celery import Task

from djcelery.celery_config import app

"""
from djcelery.celery_tasks.ex2_custom_tasks_class import my_task
my_task.delay()
"""

logging.basicConfig(
    filename="app.log", level=logging.ERROR, format="%(actime)s %(levelname)s %(message)s"
)


class CustomTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if isinstance(exc, ConnectionError):
            logging.error("Connection error occurred....Admin Notified")
        else:
            print("{0!r} failed: {1!r}".format(task_id, exc))
            # Perform additional error handling actions if needed


app.Task = CustomTask


@app.task(queue="tasks")
def my_task():
    try:
        raise ConnectionError("Connection Error Occured...")
    except ConnectionError:
        logging.error("Connection error occurred....")
        raise ConnectionError()
    except ValueError:
        # Handle value error
        logging.error("Value error occurred...")
        # Perform specific error handling actions
        perform_specific_error_handing()
    except Exception:
        # Handle generic exceptions
        logging.error("An error occured")
        # Notify administrators or perform fallback action
        notify_admins()
        perform_specific_error_handing()


def perform_specific_error_handing():
    # Logic to handle a specific error scenario
    pass


def notify_admins():
    # Logic to send notifications to administrators
    pass
