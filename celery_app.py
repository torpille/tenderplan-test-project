from celery import Celery

app = Celery('my_app', broker='redis://localhost:6379/0',
             result_backend='redis://localhost:6379/0')
app.autodiscover_tasks(['tasks'])
