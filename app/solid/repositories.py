# api/repositories.py
from app.models import Record
from django.core.exceptions import ObjectDoesNotExist

class RecordRepository:
    def get_all_records(self):
        return Record.objects.all()

    def get_record_by_id(self, record_id):
        try:
            return Record.objects.get(id=record_id)
        except Record.DoesNotExist:
            return None

    def create_record(self, record_data):
        return Record.objects.create(**record_data)

    def update_record(self, record_id, record_data):
        record = self.get_record_by_id(record_id)
        if record:
            for key, value in record_data.items():
                setattr(record, key, value)
            record.save()
            return record
        return None

    def delete_record(self, record_id):
        record = self.get_record_by_id(record_id)
        if record:
            record.delete()
            return True
        return False
