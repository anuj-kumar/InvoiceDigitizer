from django.core.cache import cache

from digifier.constants import QUEUED_STATUS, DIGITIZATION_CACHE_PREFIX
from digifier.models import Document


class DigitizationHelper(object):

    @staticmethod
    def initiate_digitization(doc: Document):
        DigitizationCacheLayer.set(doc.pk, QUEUED_STATUS)
        from digifier.tasks import digitization_task
        digitization_task.delay(doc.pk)


class DigitizationCacheLayer(object):

    @classmethod
    def get(cls, doc_id: int):
        key = cls._get_cache_key(doc_id)
        return cache.get(key)

    @classmethod
    def set(cls, doc_id: str, status: str):
        key = cls._get_cache_key(doc_id)
        cache.set(key, status)

    @classmethod
    def _get_cache_key(cls, suffix):
        key = "{}_{}".format(DIGITIZATION_CACHE_PREFIX, suffix)
        return key
