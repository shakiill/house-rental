from django.contrib.auth.decorators import login_required
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('dashboard/', login_required(views.DashboardView.as_view()), name='dashboard'),
    path('', views.HomeView.as_view(), name='home'),
]