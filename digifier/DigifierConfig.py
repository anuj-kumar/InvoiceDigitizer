from django.apps import AppConfig


class DigifierConfig(AppConfig):
    name = 'digifer'

    def ready(self):
        from .celery import googleimport as google_import
