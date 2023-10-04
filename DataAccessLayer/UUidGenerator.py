import uuid


class UuidGenerator:
    @staticmethod
    def generate():
        new_uuid = str(uuid.uuid4())
        return new_uuid
