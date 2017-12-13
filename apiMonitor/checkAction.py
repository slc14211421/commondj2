import  requests
import simplejson

def checkMarket(hostip):
    port="8070"
    suburl="/market/interface/getVoteItem?customertype=2&customerno=&terminaltype=TV&sorttype=0&eventid=744"
    checkurl="http://"+hostip+":"+port+suburl

    try:
        res=requests.get(url=checkurl)
        if res.status_code == 200 :
            resdic=simplejson.JSONDecoder().decode(res.content)
            if resdic['result']['errorcode'] == "2" :
                return "SUCESS"
            else:
                return "FAILED"
        else:
            return "FAILED"
    except:
        return "FAILED"