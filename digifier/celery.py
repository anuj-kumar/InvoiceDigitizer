import os
from celery import Celery
from django.conf import settings


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digifier.settings')

app = Celery('digifier')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')

app.autodiscover_tasks(list(settings.INSTALLED_APPS))


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
