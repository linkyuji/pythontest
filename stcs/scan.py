#coding = utf-8
import optparse
import socket
def connScan(tgtHost,tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # connSkt.connect(tgtHost)
        connSkt.connect((tgtHost,tgtPort))
        print '[+]'+str(tgtPort)+'/tcp open'
        connSkt.close()
    except:
        print '[-]'+str(tgtPort)+'/tcp close'

def portScan(tgtHost,tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
        print tgtIP
    except:
        print "[-]Cannot resolve"+tgtHost+":Unknow host"
        return
    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: ' + tgtName[0])
    except:
        print('\n[-] Scan Results for: ' + tgtIP)
    socket.setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning port ' + str(tgtPort))

        connScan(tgtHost, int(tgtPort))

portScan('www.baidu.com',[21,20,80,443,3389,1433,23,445])