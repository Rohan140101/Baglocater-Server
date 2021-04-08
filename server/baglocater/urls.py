from django.urls import path
from . import views

urlpatterns = [
    path('', views.decode, name='decode')
]