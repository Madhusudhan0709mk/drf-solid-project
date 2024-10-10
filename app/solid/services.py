
class RecordService:
    def __init__(self, record_repository):
        self.record_repository = record_repository

    def list_all_records(self):
        return self.record_repository.get_all_records()

    def retrieve_record(self, record_id):
        return self.record_repository.get_record_by_id(record_id)

    def create_record(self, record_data):
        return self.record_repository.create_record(record_data)

    def update_record(self, record_id, record_data):
        return self.record_repository.update_record(record_id, record_data)

    def delete_record(self, record_id):
        return self.record_repository.delete_record(record_id)
