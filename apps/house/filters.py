import django_filters

from apps.house.forms import ApartmentFiltersForm
from apps.house.models import Apartment


class ApartmentFilters(django_filters.FilterSet):
    # title = django_filters.CharFilter(method='project_filter')

    class Meta:
        model = Apartment
        fields = ['rent', 'room', 'floor', 'parking', 'lift', 'district', 'thana', 'union', ]
        form = ApartmentFiltersForm

    # def project_filter(self, queryset, title, value):
    #     return queryset.filter(title__icontains=value)
