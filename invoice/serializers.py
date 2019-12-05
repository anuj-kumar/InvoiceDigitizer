from rest_framework import serializers

from .models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['number', 'vendor', 'buyer', 'generated_at', 'currency', 'amount', 'items']
