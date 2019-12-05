from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import InvoiceSerializer
from .models import Invoice


class DigitalInvoiceView(APIView):

    def put(self, request, invoice_id):
        try:
            invoice = Invoice.objects.get(pk=invoice_id)
        except Invoice.DoesNotExist:
            return Response({
                'message': 'invalid invoice ID'
            }, status=status.HTTP_400_BAD_REQUEST)

        invoice_serializer = InvoiceSerializer(invoice, data=request.data)
        if invoice_serializer.is_valid():
            invoice_serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, invoice_id):
        try:
            invoice = Invoice.objects.get(pk=invoice_id)
        except Invoice.DoesNotExist:
            return Response({
                'message': 'Invoice not found'
            }, status=status.HTTP_404_NOT_FOUND)

        invoice_serializer = InvoiceSerializer(invoice)
        return Response(invoice_serializer.data)
