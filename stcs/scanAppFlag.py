#coding = utf-8
import optparse
import socket
def connScan(tgtHost,tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send('python')
        results = connSkt.recv(100)
        print "[+]"+str(tgtPort)+"/tcp open"
        print "[+]" + str(results)
        connSkt.close()
    except:
        print '[-]'+str(tgtPort)+'/tcp close'

def portScan(tgtHost,tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
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

def main():
   parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
   parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
   parser.add_option('-p', dest='tgtPort', type='int', help='specify target port')
   (options, args) = parser.parse_args()
   tgtHost = options.tgtHost
   tgtPort = options.tgtPort
   args.append(tgtPort)
   if (tgtHost == None) | (tgtPort == None):
       print('[-] You must specify a target host and port[s]!')
       exit(0)
   else:
       portScan(tgtHost, args)

if __name__ == '__main__':
    main()
    print 'final'