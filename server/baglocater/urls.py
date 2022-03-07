from django.urls import path
from . import views

urlpatterns = [
    path('decode', views.decode, name='decode'),
    path('authenticate', views.authenticate, name='authenticate'),
    path('addLostAndFound', views.addLostAndFound, name='addLostAndFound'),
    path('searchBags', views.searchBags, name='searchBags')
]
