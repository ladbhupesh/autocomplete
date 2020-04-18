
from django.urls import path
from geocode import views

urlpatterns = [
    path('', views.geoview, name='geo'),
    path('coordinate-autocomplete/<geocode>', views.getgeocode, name='coordinate-autocomplete'),
]
