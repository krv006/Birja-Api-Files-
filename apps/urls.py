from django.urls import path
from .views import (
    FileCodeGenerateAPIView,
    FileUploadWithCodeAPIView,
    FileDownloadByCodeAPIView,
)

urlpatterns = [
    path('generate_code/', FileCodeGenerateAPIView.as_view()),
    path('upload_by_code/', FileUploadWithCodeAPIView.as_view()),
    path('download_by_code/<str:file_code>/', FileDownloadByCodeAPIView.as_view()),
]
