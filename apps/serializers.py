from rest_framework import serializers
from .models import OrganizationFile


class OrganizationFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationFile
        fields = '__all__'
        read_only_fields = ['id', 'uploaded_at', 'file_code']


class FileCodeGenerateSerializer(serializers.Serializer):
    owner_id = serializers.UUIDField()

class FileCodeSubmitSerializer(serializers.Serializer):
    file_code = serializers.CharField()
    file = serializers.FileField()
