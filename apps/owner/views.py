# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView

from apps.helpers.views import PageHeaderMixin
from apps.house.models import Apartment
from apps.owner.forms import MyApartmentForm


class MyApartmentListView(ListView):
    model = Apartment
    paginate_by = 20
    ordering = '-created_at'
    template_name = 'my_apartments.html'

    def get_queryset(self):
        qs = self.queryset
        qs = qs.filter(owner=self.request.user)
        return qs


class MyApartmentCreateView(CreateView):
    model = Apartment
    form_class = MyApartmentForm
    template_name = 'add.html'
    success_url = reverse_lazy('my_apartments')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MyApartmentUpdateView(UpdateView):
    model = Apartment
    form_class = MyApartmentForm
    template_name = 'add.html'
    success_url = reverse_lazy('my_apartments')


class MyApartmentDeleteView(PageHeaderMixin, DeleteView):
    model = Apartment
    template_name = 'delete.html'
    page_title = 'Buyer'
    success_url = reverse_lazy('my_apartments')
