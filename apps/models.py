import uuid
from django.core.exceptions import ValidationError
from django.db.models import Model, CharField, UUIDField, DateTimeField, FileField, IntegerField


class Organization(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


def upload_to(instance, filename):
    return f"templates/{str(instance.owner_id)}/{filename}"


class OrganizationFile(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner_id = UUIDField()
    file_name = CharField(max_length=255)
    file_path = FileField(upload_to=upload_to, max_length=500)
    file_type = IntegerField(default=0)
    template_id = UUIDField(null=True, blank=True)
    parent_id = UUIDField(null=True, blank=True)
    uploaded_at = DateTimeField(auto_now_add=True)

    file_code = CharField(max_length=50, unique=True, null=True, blank=True)  # <- ADD THIS

    def __str__(self):
        return self.file_name

    def clean(self):
        max_size = 100 * 1024 * 1024  # 100MB
        if self.file_path and self.file_path.size > max_size:
            raise ValidationError("Fayl hajmi 100MB dan oshmasligi kerak.")
