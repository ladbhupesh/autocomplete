from django.http import HttpResponse
from django.shortcuts import render

from geocode.forms import CoordinateForm
from geocode.models import Coordinate


def geoview(request):
    form = CoordinateForm()
    if request.method == "POST":

        return render(request, 'index.html',{"form":form,"res":request.POST["code"]})

    return render(request, 'index.html',{"form":form})


def getgeocode(request, geocode):
    results = Coordinate.objects.filter(code__istartswith=str(geocode))
    sendres = ""
    for resn in results[:10]:
        sendres += "<option class='bg-primary'>" + resn.code + "</option>"
    return HttpResponse(sendres)
# Create your views here.
