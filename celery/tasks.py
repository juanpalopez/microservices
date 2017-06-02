from celery import Celery
from requests import get

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y

@app.task
def getData(facebook_page_id):
    return 'Fetching data from {}'.format(facebook_page_id)
