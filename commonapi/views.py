from django.shortcuts import render
from django.http import request,HttpResponse
from commonapi.models import t_stburls
import simplejson
from commonapi.myaction import *
import logging
logger = logging.getLogger("django")


def geturl(request):
    logger.info("geturl request receiver")
    if request.method == 'GET':
        result =dogeturl2(request.GET.get('stbnum'))
        return HttpResponse(simplejson.dumps(result))
    else:
        return HttpResponse("This is Juest for HTTP GET")

def seturl(request):
    if request.method == 'POST':
        try:
            stbnum=request.POST['stbnum']
            url=request.POST['url']
            stu=t_stburls(stbnum=stbnum,url=url)
            stu.save()
            return  HttpResponse("SUCESS")
        except:
            return HttpResponse("Failed")
    else:
        return HttpResponse("This API is Juest for HTTP POST ")


