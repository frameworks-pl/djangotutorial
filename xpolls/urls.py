from django.urls import path

from . import views

urlpatterns = [
    path('', views.xindex, name='xindex'),
]