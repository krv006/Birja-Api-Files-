from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.models import OrganizationFile, Organization


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class OrganizationFileSerializer(ModelSerializer):
    class Meta:
        model = OrganizationFile
        fields = '__all__'

    def validate_file_path(self, file):
        max_size = 100 * 1024 * 1024  # 100MB
        if file.size > max_size:
            raise ValidationError("Fayl hajmi 100MB dan oshmasligi kerak.")
        return file
