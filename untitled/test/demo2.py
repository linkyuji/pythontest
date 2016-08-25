#coding:utf-8
import urllib2
import urllib
#post爬虫

url = 'https://www.zhihu.com/#signin'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
values = {'phone_num':'17764526457', 'password':'zrh17909'}
headers = { 'User-Agent' : user_agent }
data = urllib.urlencode(values)
request = urllib2.Request(url,data=data,headers=headers)
response = urllib2.urlopen(request)
print response.read()