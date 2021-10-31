from django import views
from django.urls import path

from recommender_system.views import searchresult
from . import views

urlpatterns = [
    path('',views.searchresult, name='recommender_system'),
]   