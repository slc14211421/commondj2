from django.shortcuts import render
from django.http import request,HttpResponse
import requests
from . import checkAction

# Create your views here.

def checkApi(request):
    if request.method == 'GET':

        projectNname = request.GET.get('project')
        hostip = request.GET.get('hostip')
        if projectNname == "market":
            result = checkAction.checkMarket(hostip)

        if projectNname == "portalProxy":
            result = checkAction.checkPortalProxy(hostip)

        return HttpResponse(result)
    else:
        return HttpResponse("This is Juest for HTTP GET")



