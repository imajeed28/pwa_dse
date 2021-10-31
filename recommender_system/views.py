from django.shortcuts import render
from django.views import View
from django.http import request
from .models import RecommendationSystemModel
# Create your views here.

def searchresult(request):
    if request.method=="POST":
            # frompercentage=request.POST.get("frompercentage")
            # topercentage=request.POST.get("topercentage")
            from_percentage=request.POST.get("from_percentage")
            to_percentage=request.POST.get("to_percentage")
            seat_type1=request.POST.get("seat_type1")
            seat_type2=request.POST.get("seat_type2")
            seat_type3=request.POST.get("seat_type3")
            course1=request.POST.get("course1")
            course2=request.POST.get("course2")
            course3=request.POST.get("course3")
            course4=request.POST.get("course4")
            course5=request.POST.get("course5")
            course6=request.POST.get("course6")
            college_status7=request.POST.get("college_status7")
            college_status8=request.POST.get("college_status8")
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
            minority1=request.POST.get("minority1")
            minority2=request.POST.get("minority2")
            # college location conditional statement
            if (seat_type2==None):
                seat_type2=request.POST.get("seat_type1")
            else:
                seat_type2=request.POST.get("seat_type2")
            if (course4==None):
                course4=request.POST.get("course1")
            else:
                course4=request.POST.get("course4")
            if (course5==None):
                course5=request.POST.get("course1")
            else:
                course5=request.POST.get("course5")
            
            if (course6==None):
                course6=request.POST.get("course1")
            else:
                course6=request.POST.get("course6")

            if (college_location3==None):
                college_location3=request.POST.get("college_location1")
            else:
                college_location3=request.POST.get("college_location3")

            # college status conditional statement 
            if (college_status6==None):
                college_status6=request.POST.get("college_status1")
            else:
                college_status6=request.POST.get("college_status6")
            if (college_status7==None):
                college_status7=request.POST.get("college_status1")
            else:
                college_status7=request.POST.get("college_status7")
            if (college_status8==None):
                college_status8=request.POST.get("college_status1")
            else:
                college_status8=request.POST.get("college_status8")
            if(minority2==None):
                minority2=request.POST.get("minority1")
            else:
                minority2=request.POST.get("minority2")
            # college_location=request.POST.get("college_location")
            # status=request.POST.get("status")
            # minority=request.POST.get("minority")
            search_result=RecommendationSystemModel.objects.raw('select * from recommendation_system_21 where percentage between "'+from_percentage+'" and "'+to_percentage+'" and seat_type in("'+seat_type1+'","'+seat_type2+'","'+seat_type3+'") and course_name in("'+course1+'","'+course2+'","'+course3+'","'+course4+'","'+course5+'","'+course6+'") and college_location in("'+college_location1+'","'+college_location2+'","'+college_location3+'") and status in("'+college_status1+'","'+college_status2+'","'+college_status3+'","'+college_status4+'","'+college_status5+'","'+college_status6+'","'+college_status7+'","'+college_status8+'") and minority in("'+minority1+'","'+minority2+'") order by percentage DESC')
            context={
                'data':search_result
            }
            return render(request, 'recommender_system/recommender_system.html',context)
    else:
         return render(request, 'recommender_system/recommender_system.html')

# percentage between "'+frompercentage+'" and "'+topercentage+'"  and
# and college_location="'+str(college_location)+'"
