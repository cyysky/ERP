from .models import BOM
import django_filters
class BOMFilter(django_filters.FilterSet):
    class Meta:
       model = BOM
       fields = '__all__'