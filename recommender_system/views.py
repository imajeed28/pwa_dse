from django.shortcuts import render
from django.views import View
# Create your views here.

class Recommender_system(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'recommender_system/recommender_system.html')
# Create your views here.
