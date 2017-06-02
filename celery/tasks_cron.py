from celery import Celery
from celery.schedules import crontab

app = Celery()
app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-morning': {
        'task': 'tasks.add',
        'schedule': crontab(minute='*'),
        'args': (16, 16),
    },
    'fetching-every-morning': {
        'task': 'tasks.getData',
        'schedule': crontab(minute='*'),
        'args': (327026330836426,),
    },
}
