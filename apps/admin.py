from django.contrib import admin

from apps.models import Organization, OrganizationFile

admin.site.register(Organization)
admin.site.register(OrganizationFile)