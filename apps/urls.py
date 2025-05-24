from django.urls import path
from apps.views import OrganizationFileListCreateView

urlpatterns = [
    path('organization_files/', OrganizationFileListCreateView.as_view(), name='organization_files'),
]
