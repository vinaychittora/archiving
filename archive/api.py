from tastypie.resources import ModelResource
from archive.models import Archive


class ArchiveResource(ModelResource):
    class Meta:
        queryset = Archive.objects.all()
        resource_name = 'archive'
