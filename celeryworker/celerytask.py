from celery import Celery

app = Celery('tasks')
app.config_from_object('celeryconfig')
app.conf.imports = ('cworker.tasks')
app.autodiscover_tasks()
