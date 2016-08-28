#coding=utf-8
import zipfile
import threading
def extractFile(zFile,password):
    try:
        zFile.extractall(pwd = password)
        print "password is " + password
        return password
    except:
        pass

def main():
    zFile = zipfile.ZipFile('passwords.zip')
    passFile = open('dictionary.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        # guess = extractFile(zFile,password)
        # =======多线程=======
        t = threading.Thread(target=extractFile,args=(zFile,password))
        t.start()
if __name__ == '__main__':
    main()