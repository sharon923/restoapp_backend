from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from resto.serializer import RestoSerializer
from resto.models import RestoModel
from django.db.models import Q


# Create your views here.
@csrf_exempt
def viewRest(request):
        if request.method == "POST":
                resto_list = RestoModel.objects.all()
                serialized_data= RestoSerializer(resto_list, many=True)
                return HttpResponse(json.dumps(serialized_data.data))
@csrf_exempt
def addRest(request):
        if request.method == "POST":
                recieved_data = json.loads(request.body)
                print(recieved_data)
                serializer_check=RestoSerializer(data=recieved_data)
                if serializer_check.is_valid():
                        serializer_check.save()
                        return HttpResponse(json.dumps({"status":"success"}))
                else:
                        return HttpResponse(json.dumps({"status":"failed"}))
                
@csrf_exempt
def searchRest(request):
        if request.method == "POST":
                recieved_data = json.loads(request.body)
                getName = recieved_data["name"]
                data = list(RestoModel.objects.filter(Q(name__icontains = getName)).values())
                return HttpResponse(json.dumps(data))
