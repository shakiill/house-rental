from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', login_required(views.DashboardView.as_view()), name='dashboard'),
    path('', views.HomeView.as_view(), name='home'),

    path('apartment/', login_required(views.ApartmentListView.as_view()), name='apartments'),
    path('apartment/add/', login_required(views.ApartmentCreateView.as_view()), name='apartment_add'),
    path('apartment/<int:pk>/update/', login_required(views.ApartmentUpdateView.as_view()),
         name='apartment_update'),
    path('apartment/<int:pk>/delete/', login_required(views.ApartmentDeleteView.as_view()),
         name='apartment_delete'),
]
