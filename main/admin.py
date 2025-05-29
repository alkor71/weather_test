from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from .models import City
from .resources import CityResource


@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    resource_class = CityResource
    list_display = ('name',)
    search_fields = ('name',)
