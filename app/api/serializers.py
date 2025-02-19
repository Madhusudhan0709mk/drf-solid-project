from rest_framework import serializers
from app.models import Record

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']