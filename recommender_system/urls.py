from django import views
from django.urls import path

from recommender_system.views import searchresult, compareresult, placement
from . import views

urlpatterns = [
    path('',views.searchresult, name='recommender_system'),
    path('college_comparison/',views.compareresult, name='college_comparison'),
    path('placement/',views.placement, name='placement'),
]   