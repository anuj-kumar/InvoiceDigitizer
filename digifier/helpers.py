from django.core.cache import cache

from digifier.constants import QUEUED_STATUS, DIGITIZATION_CACHE_PREFIX
from digifier.models import Document


class DigitizationHelper(object):

    @staticmethod
    def initiate_digitization(doc: Document):
        """
        Initiate digitization of a doc
        The status is updated in the cache while the doc is submitted in the queue for digitization
        Args:
            doc: Document object to be digitized

        Returns:
            None

        """
        DigitizationCacheLayer.set(doc.pk, QUEUED_STATUS)
        from digifier.tasks import digitization_task
        digitization_task.delay(doc.pk)


class DigitizationCacheLayer(object):
    """
    Layer above Django's cache to perform additional repetitive work such as cache key generation
    """

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
        """
        Returns appropriate cache key based on the suffix
        Args:
            suffix: suffix to be used in the cache key

        Returns:
            final key to be used in cache

        """
        key = "{}_{}".format(DIGITIZATION_CACHE_PREFIX, suffix)
        return key
