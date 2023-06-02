import socket
import requests
import urllib.requests
import jieba
from lxml import etree
def search(name:str) :->str
  nali=jieba.cut(name)
  for i in nali:
    url = "https://baike.baidu.com/item/"+i
    
    r = requests.get(url)#获得服务器响应
    html_code = r.content.decode(r.encoding)#解码
    
    treeObj = etree.HTML(html_code)
    target = treeObj.xpath("//div[@class='para MARK_MODULE']/div[@data_pid='1']/p/span[@class='short']/text()")
    return target
