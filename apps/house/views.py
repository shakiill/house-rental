from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from apps.helpers.views import PageHeaderMixin
from apps.house.filters import ApartmentFilters
from apps.house.forms import ApartmentForm
from apps.house.models import Apartment


# Create your views here.
class DashboardView(TemplateView):
    template_name = 'home.html'


class ApartmentListView(FilterView):
    model = Apartment
    filterset_class = ApartmentFilters
    paginate_by = 20
    ordering = '-created_at'
    template_name = 'apartments.html'


class ApartmentCreateView(CreateView):
    model = Apartment
    form_class = ApartmentForm
    template_name = 'add.html'
    success_url = reverse_lazy('apartments')

    # def form_valid(self, form):
    #     form.instance.owner = self.request.user
    #     return super().form_valid(form)


class ApartmentUpdateView(UpdateView):
    model = Apartment
    form_class = ApartmentForm
    template_name = 'add.html'
    success_url = reverse_lazy('apartments')


class ApartmentDeleteView(PageHeaderMixin, DeleteView):
    model = Apartment
    template_name = 'delete.html'
    page_title = 'apartments'
    success_url = reverse_lazy('apartments')


# public

class HomeView(TemplateView):
    template_name = 'index.html'


class PublicApartmentListView(FilterView):
    model = Apartment
    filterset_class = ApartmentFilters
    paginate_by = 20
    ordering = '-created_at'
    template_name = 'all_apartments.html'
