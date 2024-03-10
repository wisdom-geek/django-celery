from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')

app = Celery('django_celery_project')

app.config_from_object(settings, namespace='CELERY')

#Configure beat settings
app.conf.beat_schedule = {
    
}

app.autodiscover_tasks()


app.task(bind = True)

def deaug_task(self):
    print(f'Request: {self.requset!r}')