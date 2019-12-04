from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework import status

from digifier.helpers import DigitizationHelper, DigitizationCacheLayer
from .serializers import DocumentSerializer


class DigitizationView(APIView):

    parser_class = FileUploadParser

    def post(self, request):
        doc_serializer = DocumentSerializer(data=request.data)
        instance = None
        if doc_serializer.is_valid():
            instance = doc_serializer.save()
        else:
            # log this incident
            return Response(status=status.HTTP_400_BAD_REQUEST)

        DigitizationHelper.initiate_digitization(instance)
        return Response({
            'doc_id': instance.pk
        }, status=status.HTTP_202_ACCEPTED)


class DigitizationStatusView(APIView):

    def get(self, request, doc_id):
        status = DigitizationCacheLayer.get(doc_id)
        # Exception handling
        return Response({
            'digitization_status': status
        })

    def put(self, request, document_id):
        pass
