# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
class BT:

    #初始化，传入基地址
    def __init__(self,baseUrl,title):
        #base链接地址

        self.baseURL = baseUrl
        self.page = 1
        self.title = title

    def getmagnet(self, url):

        try:
            url = 'http://www.btmeet.com/'+url
            print url
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            headers = {'User-Agent': user_agent}
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request)
            # 返回UTF-8格式编码内容

            html =  response.read().decode('utf-8')
            pattern = re.compile('"magnet(.*?)"', re.S)
            x = re.finditer(pattern, html)
            for m in x:
                item = m.group()
            return item
        # 无法连接，报错
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接失败,错误原因",e.reason
                return None


    def replace(self,item):
        pattern = re.compile('/wiki(.*?)html', re.S)
        x = re.finditer(pattern, item)
        for m in x:
           item = m.group()
        return item

    #传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            #构建URL
            url = self.baseURL+'/' + str(pageNum) + '-1'
            print url
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            headers = {'User-Agent': user_agent}
            request = urllib2.Request(url,headers = headers)
            response = urllib2.urlopen(request)
            #返回UTF-8格式编码内容

            return response.read().decode('utf-8')
        #无法连接，报错
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接失败,错误原因",e.reason
                return None

    # 获取每一层的内容,传入页面内容
    def getContent(self, page):
        # 匹配所有楼层的内容
        # print page
        pattern = re.compile('<div class="item-title">(.*?)</div>', re.S)

        items = re.findall(pattern, page)
        contents = []
        for item in items:
            # 将url去除标签，组装访问后返回magnet
            i = self.replace(item)
            content = "\n" + self.getmagnet(i) + "\n"
            contents.append(content.encode('utf-8'))
        return contents

    def writeData(self,contents):
        #向文件写入每一楼的信息
        for item in contents:
            floorLine = "\n"  + u"-----------------------------------------------------------------------------------------\n"
            self.file.write(floorLine)
            self.file.write(item)


    def setFileTitle(self,title):
        #如果标题不是为None，即成功获取到标题
        if title is not None:
            self.file = open(title + ".txt","w+")
        else:
            self.file = open(self.defaultTitle + ".txt","w+")

    def start(self):
        indexPage = self.getPage(self.page)
        self.setFileTitle(self.title)

        try:
            print "共有 1 页"

            print "正在写入第 1 页数据"
            page = self.getPage(1)
            contents = self.getContent(page)
            self.writeData(contents)
        #出现写入异常
        except IOError,e:
            print "写入异常，原因" + e.message
        finally:
            print "写入任务完成"

print u"请输入帖子代号"
title = 'SwordArtOnline'
baseURL = 'http://www.btmeet.com/search/'+title
# baseURL = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))
# http://www.btcherrycn.com/search-kw-123-p-2.html
bt = BT(baseURL,title)
bt.start()