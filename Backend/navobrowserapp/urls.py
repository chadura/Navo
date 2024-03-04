# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    # Add other paths here as needed
]
