from import_export import resources
from .models import City


class CityResource(resources.ModelResource):
    class Meta:
        model = City
        fields = ('name',)  # импортируем только поле name
        import_id_fields = ['name']  # уникальное поле для обновления/создания
        skip_unchanged = True
        report_skipped = True
