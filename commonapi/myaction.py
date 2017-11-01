
from django.db import connection
from .models import t_stburls

def dogeturl2(stbnum):
    result = {}
    result['stbnum'] = stbnum
    if (stbnum != None) and (stbnum != ""):
        stburl=t_stburls.objects.filter(stbnum=stbnum).order_by('-pkid')[:1]
        if len(stburl) > 0:
            result['url'] = stburl[0].url
            result['status'] = "SUCESS"
        else:
            result['status'] = "Failed"
            result['errmessage'] = "stbnum %s is not exist" % (stbnum)
    else:
        result['status'] = "Failed"
        result['errmessage'] = "request stbnum"
    return result



def dogeturl(stbnum):
    result = {}
    result['stbnum'] = stbnum
    if (stbnum != None) and (stbnum != ""):
        querysql = "select url from commonapi_t_stburls where stbnum='" + stbnum + "' order by pkid desc limit 1"
        cursor = connection.cursor()
        cursor.execute(querysql)
        row = cursor.fetchone()
        if row != None:
            result['url'] = row[0]
            result['status'] = "SUCESS"
        else:
            result['status'] = "Failed"
            result['errmessage'] = "stbnum %s is not exist" % (stbnum)
    else:
        result['status'] = "Failed"
        result['errmessage'] = "request stbnum"
    return result