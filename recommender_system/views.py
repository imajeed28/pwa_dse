from django.shortcuts import render
from django.views import View
from django.http import request
from .models import RecommendationSystemModel
# Create your views here.

def searchresult(request):
    if request.method=="POST":
            # frompercentage=request.POST.get("frompercentage")
            # topercentage=request.POST.get("topercentage")
            college_location=request.POST.get("college_location")
            # college_location=request.POST.get("college_location")
            # status=request.POST.get("status")
            # minority=request.POST.get("minority")
            search_result=RecommendationSystemModel.objects.raw(
                ' select * from recommendation_system_21 where college_location = '+str(college_location)+''
            )
            context={
                'data':search_result
            }
            return render(request, 'recommender_system/recommender_system.html',context)
    else:
        return render(request, 'recommender_system/recommender_system.html')

# percentage between "'+frompercentage+'" and "'+topercentage+'"  and
# and college_location="'+str(college_location)+'"
