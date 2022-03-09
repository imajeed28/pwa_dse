from django import views
from django.urls import path

from prediction.views import predictresult
from . import views

urlpatterns = [
    path('',views.predictresult, name='prediction'),
]   