from celery import Celery

app = Celery('my_app', broker='redis://redis:6379/0',
             result_backend='redis://redis:6379/0')
app.autodiscover_tasks(['tasks'])
