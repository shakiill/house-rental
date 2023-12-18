from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('my_apartment/', login_required(views.MyApartmentListView.as_view()), name='my_apartments'),
    path('my_apartment/add/', login_required(views.MyApartmentCreateView.as_view()), name='my_apartment_add'),
    path('my_apartment/<int:pk>/update/', login_required(views.MyApartmentUpdateView.as_view()),
         name='my_apartment_update'),
    # path('my_apartment/<int:pk>/view/', login_required(views.MyApartmentView.as_view()),
    #      name='my_apartment_view'),
    path('my_apartment/<int:pk>/delete/', login_required(views.MyApartmentDeleteView.as_view()),
         name='my_apartment_delete'),
]
