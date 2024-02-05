# from celery import Celery
# from celery import shared_task
# app = Celery('tasks', broker='redis://localhost')
#
# @shared_task
# def add():
#     return 'hello mother_fucker!!!'


from celery import Celery

app = Celery('tasks', broker='redis://guest@localhost//')

@app.task
def add(x, y):
    return x + y
