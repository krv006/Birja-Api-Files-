import uuid
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OrganizationFile
from .serializers import (
    OrganizationFileUploadSerializer,
    FileCodeGenerateSerializer,
    FileCodeSubmitSerializer,
)
from django.shortcuts import get_object_or_404
from django.http import FileResponse


# STEP 1 - Generate code
class FileCodeGenerateAPIView(APIView):
    def post(self, request):
        serializer = FileCodeGenerateSerializer(data=request.data)
        if serializer.is_valid():
            file_code = str(uuid.uuid4()).replace("-", "")[:16]
            OrganizationFile.objects.create(
                owner_id=serializer.validated_data['owner_id'],
                file_name="",
                file_code=file_code
            )
            return Response({"file_code": file_code}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# STEP 2 - Upload file using file_code
class FileUploadWithCodeAPIView(APIView):
    def post(self, request):
        serializer = FileCodeSubmitSerializer(data=request.data)
        if serializer.is_valid():
            file_code = serializer.validated_data['file_code']
            org_file = get_object_or_404(OrganizationFile, file_code=file_code)

            org_file.file_path = serializer.validated_data['file']
            org_file.file_name = org_file.file_path.name
            org_file.save()

            return Response({"file_path": org_file.file_path.url}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# STEP 3 - Download file by file_code
class FileDownloadByCodeAPIView(APIView):
    def get(self, request, file_code):
        org_file = get_object_or_404(OrganizationFile, file_code=file_code)
        if not org_file.file_path:
            return Response({"error": "Fayl mavjud emas"}, status=status.HTTP_404_NOT_FOUND)
        file_path = org_file.file_path.path
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=org_file.file_name)
