# api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.solid.services import RecordService
from app.solid.repositories import RecordRepository
from app.api.serializers import RecordSerializer

class RecordView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Inject RecordRepository into RecordService
        self.record_service = RecordService(RecordRepository())

    # List
    def get(self, request, record_id=None):
        if record_id:
            record = self.record_service.retrieve_record(record_id)
            if record:
                serializer = RecordSerializer(record)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)
        records = self.record_service.list_all_records()
        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create
    def post(self, request):
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            record = self.record_service.create_record(serializer.validated_data)
            return Response(RecordSerializer(record).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Update
    def put(self, request, record_id):
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            record = self.record_service.update_record(record_id, serializer.validated_data)
            if record:
                return Response(RecordSerializer(record).data, status=status.HTTP_200_OK)
            return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete
    def delete(self, request, record_id):
        deleted = self.record_service.delete_record(record_id)
        if deleted:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)
