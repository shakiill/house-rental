import django_filters
from django_filters.widgets import RangeWidget

from apps.location.models import District


class ProjectFilters(django_filters.FilterSet):
    title = django_filters.CharFilter(method='project_filter')

    class Meta:
        model = Projects
        fields = ['title', ]
        form = ProjectFiltersForm

    def project_filter(self, queryset, title, value):
        return queryset.filter(title__icontains=value)