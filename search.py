#coding=utf-8
import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)  #urllib.urlopen()方法用于打开一个URL地址
    html = page.read().decode("UTF-8") #read()方法用于读取URL上的数据
    return html

head = "http://music.163.com/song?id="
root = 534556
reg = r'(?<=data-res-name=").*?(?=")'
imgre = re.compile(reg)
f = open("music.txt","w+")

while root <= 99999999:
    html = getHtml(head+str(root))
    imglist = re.findall(imgre, html)
    root += 1
    try:
        if (imglist[0][0] != '$' and imglist[0][0] != '{'):
            f.write(str(root) + " ")
            f.write(imglist[0] + "\n")
    except:
        continue
f.close()


