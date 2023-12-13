#coding = utf-8
try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")
from os.path import exists
from tkinter import E
import urllib
import urllib.request as urllib2
import chardet  #<- import this lib
import os

Key_file_name = "key.txt"
conf_file_name = "conf.txt"



# to search
def savetohtml(root, index,url):
    req = urllib2.Request(url)
    req.add_header("User-agent", "Mozilla/5.0 (Windows NT 10.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.2228.0 Safari/537.36")
    try:
        f = urllib2.urlopen(req,timeout=10) 
        html = f.read()
        
    
        f.close()
    except:
        print("urlopen failed!")
        return False
        
    
    

    charset1 = chardet.detect(html)
    print(charset1)
    encoding1 = charset1["encoding"]
    if encoding1 == None:
        encoding1 = "UTF-8"
    
    try:
        unicode_text = html.decode(encoding1)
    except:
        print("decode failed!")
        return False  
    #print("Encoding:", encoding1)     
    new_file = "{}//{}.html".format(root,index)
    f = open(new_file, 'w' ,encoding=encoding1)
    
    #page = bytes(html, 'utf-8')
    f.write(unicode_text)
    f.close()
    return True
    
    
    
    
def gsearch(root ,key, count=50):
    index =1
    for j in search(key, tld="co.kr", num=count+30, stop=count+30, pause=2):
        print(j)
        if savetohtml(root, index, j) ==True:
            index+=1
            
        if index > count:
            return True
        
        
def get_key():
    nCount = 30
    key_file_exists = exists(Key_file_name)
    if key_file_exists==False:
        print("don't exists key file")
        exit()
    
    conf_file_exists = exists(conf_file_name)
    if conf_file_exists==False:
        print("don't exists conf file")
        ##exit()
        nCount = 30
    else:
        with open(conf_file_name, 'r') as conf_file:
            try:
                nCount=int(conf_file.readline())
                if nCount<=0:
                    nCount = 30
            except:
                nCount = 30
            
    
    f=open(Key_file_name,'r',encoding="UTF-8")
    lists = f.readlines()
    key_index =1
    for key in lists :
        if key=="":
            continue
        print("*"*10,key)
        os.makedirs(str(key_index),exist_ok=True)
        gsearch(key_index, key, nCount)
        key_index+=1
    f.close()

get_key()

#savetohtml("https://naver.com")
