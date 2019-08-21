from django.contrib import admin

from archive.models import Archive
from archive.models import FileEntitiy


class FileEntityInline(admin.TabularInline):
    model = FileEntitiy


class ArchiveAdmin(admin.ModelAdmin):
    inlines = [
        FileEntityInline,
    ]


admin.site.register(Archive, ArchiveAdmin)
