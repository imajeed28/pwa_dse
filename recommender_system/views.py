from django.shortcuts import render
from django.views import View
from django.http import request
from .models import RecommendationSystemModel
# Create your views here.

def searchresult(request):
    if request.method=="POST":
            # frompercentage=request.POST.get("frompercentage")
            # topercentage=request.POST.get("topercentage")
            college_location1=request.POST.get("college_location1")
            college_location2=request.POST.get("college_location2")
            college_location3=request.POST.get("college_location3")
            college_status1=request.POST.get("college_status1")
            college_status2=request.POST.get("college_status2")
            college_status3=request.POST.get("college_status3")
            college_status4=request.POST.get("college_status4")
            college_status5=request.POST.get("college_status5")
            college_status6=request.POST.get("college_status6")
            college_status7=request.POST.get("college_status7")
            college_status8=request.POST.get("college_status8")
            # college location conditional statement
            if (college_location2==None):
                college_location2=request.POST.get("college_location1")
            else:
                college_location2=request.POST.get("college_location2")
            if (college_location3==None):
                college_location3=request.POST.get("college_location1")
            else:
                college_location3=request.POST.get("college_location3")

            # college status conditional statement  
              
            # college_location=request.POST.get("college_location")
            # status=request.POST.get("status")
            # minority=request.POST.get("minority")
            search_result=RecommendationSystemModel.objects.raw( 'select * from recommendation_system_21 where college_location in("'+college_location1+'","'+college_location2+'","'+college_location3+'") and status in("'+college_status1+'","'+college_status2+'","'+college_status3+'","'+college_status4+'","'+college_status5+'","'+college_status6+'","'+college_status7+'","'+college_status8+'")')
            context={
                'data':search_result
            }
            return render(request, 'recommender_system/recommender_system.html',context)
    else:
         return render(request, 'recommender_system/recommender_system.html')

# percentage between "'+frompercentage+'" and "'+topercentage+'"  and
# and college_location="'+str(college_location)+'"
