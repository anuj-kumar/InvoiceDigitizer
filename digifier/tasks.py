from time import sleep

from celery import shared_task

from digifier.constants import DIGITIZING_STATUS, DIGITIZED_STATUS
from digifier.helpers import DigitizationCacheLayer


@shared_task
def digitization_task(doc_id):
    DigitizationCacheLayer.set(doc_id, DIGITIZING_STATUS)
    # Submit the document for digitization here
    sleep(10)
    DigitizationCacheLayer.set(doc_id, DIGITIZED_STATUS)
