
from django.urls import path

from api_site_app import views


urlpatterns = [
    path('', views.index, name='index'),
]