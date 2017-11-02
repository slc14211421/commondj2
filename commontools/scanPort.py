#!/usr/local/bin/python
#_*_encoding:utf-8_*_

import socket
from socket import *
from threading import *
import sys


screenLock=Semaphore(value=1)
def connScan(tgtHost,tgtPort):
    try:
        connSkt=socket(AF_INET,SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send('LisonPython\r\n')
        results=connSkt.recv(100)
        screenLock.acquire()
        print '[+]%d/tcp open'% tgtPort
        print '[+] '+ results

    except:
        pass
        #print '[-]%d/tcp closed'% tgtPort
    finally:
        screenLock.release()
        connSkt.close()
def portScan(tgtHost):
    for port in range(20,65535):
        #connScan(tgtHost,port)
        thead=Thread(target=connScan,args=(tgtHost,int(port)))
        thead.start()


def main():
    if len(sys.argv) == 2 :
        portScan(sys.argv[1])
    else:
        print "eg: python scanport.py hostIp"

if __name__ == '__main__':
    main()
