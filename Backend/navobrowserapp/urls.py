# myapp/urls.py
from django.urls import path
from .views import SearchDDGView, IndexView, AutocompleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchDDGView.as_view(), name='search'),
    path('autocomplete/', AutocompleteView.as_view(), name='autocomplete'),
    # path('videosearch/', VideoSearchView.as_view(), name='video_search'),
]
