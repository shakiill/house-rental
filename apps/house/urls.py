from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('dashboard/', login_required(TemplateView.as_view(template_name="home.html")), name='dashboard'),
]