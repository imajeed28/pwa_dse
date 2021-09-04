from django.urls import path
from .views import Recommender_system

urlpatterns = [
    path('',Recommender_system.as_view(), name='recommender_system'),
]