from django.urls import path
from . import views
from .views import CityAutocomplete

urlpatterns = [
         path('', views.check_weather, name='weather'),
         path('city-autocomplete/', CityAutocomplete.as_view(), name='city-autocomplete'),
]
