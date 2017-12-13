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

def checkPortalProxy(hostip):
    port = "8070"
    suburl1 = "/portalProxy/interface/video/list?categoryId=567720&pageSize=12&pageNum=1"
    suburl2 = "/portalProxy/api/watch/listRoller?stbNo=01486617150001110&appClientType=00003"
    suburl3 = "/portalProxy/api/video/price?stbNo=99586611350156907&id=567720_2429124OOOOOOOOOOOO3"

    checkurl1 = "http://"+hostip+":"+port+suburl1
    checkurl2 = "http://"+hostip+":"+port+suburl2
    checkurl3 = "http://"+hostip+":"+port+suburl3
    checkUrls = [checkurl1, checkurl2, checkurl3]

    flag = 1

    try:
        for checkurl in checkUrls:
            res = requests.get(url=checkurl,timeout=5)
            if res.status_code == 200 :
                resdic = simplejson.JSONDecoder( ).decode(res.content)
                if resdic['status'] != "200":
                    flag = 0
                    break
            else:
                flag = 0
                break

        if flag == 1 :
            return "SUCESS"
        else:
            return "FAILED"
    except:
        return "FAILED"




