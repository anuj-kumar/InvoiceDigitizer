from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework import status

from digifier.helpers import DigitizationHelper, DigitizationCacheLayer
from .serializers import DocumentSerializer
from .constants import DIGITIZED_STATUS


class DigitizationView(APIView):

    parser_class = FileUploadParser

    def post(self, request):
        doc_serializer = DocumentSerializer(data=request.data)
        instance = None
        if doc_serializer.is_valid():
            instance = doc_serializer.save()
        else:
            # also, log this incident
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

    def put(self, request, doc_id):
        existing_cache = DigitizationCacheLayer.get(doc_id)
        if not existing_cache:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if existing_cache == DIGITIZED_STATUS:
            return Response({
                'message': 'Document already digitized'
            }, status=status.HTTP_208_ALREADY_REPORTED)

        DigitizationCacheLayer.set(doc_id, DIGITIZED_STATUS)
        return Response(status=status.HTTP_200_OK)
