from rest_framework.generics import ListCreateAPIView

from apps.models import OrganizationFile
from apps.serializers import OrganizationFileSerializer


class OrganizationFileListCreateView(ListCreateAPIView):
    serializer_class = OrganizationFileSerializer

    def get_queryset(self):
        org_id = self.request.query_params.get('orgId')
        if org_id:
            return OrganizationFile.objects.filter(owner_id=org_id)
        return OrganizationFile.objects.none()
