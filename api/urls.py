from django.urls import path
from . import views

urlpatterns = [
      path('', views.ApiOverview, name='home'),
      path('create/', views.add, name='add'),
      path('all/', views.index, name='index'),
      path('update/<int:pk>/', views.update, name='update'),
      path('delete/<int:pk>/', views.update, name='delete'),
]