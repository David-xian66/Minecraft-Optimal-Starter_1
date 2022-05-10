import requests
url = 'https://api.xiaoyistudio.top/MOS/MOS.html'

r=strhtml = requests.get(url)        #Get方式获取网页数据
r.encoding = "utf-8"
print(strhtml.text)