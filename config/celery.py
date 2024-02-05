import os
from celery import Celery
from celery.schedules import crontab

import mailing_services

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every': {
        'task': 'mailing_services.tasks.repeat_order_make',
        'schedule': crontab(), # по умолчанию выполняет каждую минуту, очень гибко
    },                                                              # настраивается

}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
