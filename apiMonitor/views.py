from django.shortcuts import render
from django.http import request,HttpResponse,HttpResponseRedirect
import requests
from . import checkAction

# Create your views here.

def checkApi(request):
    if request.method == 'GET':

        projectNname = request.GET.get('project')
        hostip = request.GET.get('hostip')
        monitorType = request.GET.get('monitorType')

        if projectNname == "market":
            result = checkAction.checkMarket(hostip)

        if projectNname == "portalProxy":
            result = checkAction.checkPortalProxy(hostip)

        if projectNname == "liuhuaPortal":
            result = checkAction.checkliuhuaPortal(hostip)

        if str(monitorType) == "hostmonitor" and result == "FAILED":
            return HttpResponseRedirect("http://www.juesterror404.com")

        return HttpResponse(result)
    else:
        return HttpResponse("This is Juest for HTTP GET")



