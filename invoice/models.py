from django.db import models

from .constants import CURRENCIES


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating created_at and updated_at fields.
    """
    created_at = models.DateTimeField('Date created', auto_now_add=True)
    updated_at = models.DateTimeField('Date updated', auto_now=True)

    class Meta:
        abstract = True


class Vendor(TimeStampedModel):
    name = models.CharField(max_length=255)
    GIN = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Buyer(TimeStampedModel):
    email = models.EmailField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.email


class Item(TimeStampedModel):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Invoice(TimeStampedModel):
    number = models.CharField(max_length=50, null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True, blank=True)
    generated_at = models.DateTimeField(null=True, blank=True)
    currency = models.CharField(max_length=3, choices=CURRENCIES, null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    items = models.ManyToManyField(Item, null=True, blank=True)
