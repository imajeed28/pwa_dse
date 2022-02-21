from django.shortcuts import render
from django.views import View
from django.http import request
from .models import PredictionModel

def predictresult(request):
    return render(request, 'prediction/prediction.html')

def predictresult(request):
    if request.method=="POST":
        college=request.POST.get("college")
        course=request.POST.get("course")
        query=PredictionModel.objects.raw('select * from cutoff_prediction where college_name = "'+college+'" and course = "'+course+'" ')
        context={
            'data1':query
        }
        return render(request, 'prediction/prediction.html',context)
    else:
        return render(request, 'prediction/prediction.html')