import requests,urllib,urllib.request,bs4,os
from bs4 import BeautifulSoup
import zipfile,logging
url='http://10.92.99.111:50000/csiroot/cservlet/DownloadLog?zip=1&file=/usr/sap/FSPRO//ppms/app//runtime'
base='http://10.92.99.111:50000/csiroot/cservlet/'

logging.basicConfig(filename='download.log',level=logging.DEBUG)

def createFolder(urlPath,currentPath):
    subName = urlPath.split('/')[-1]
    os.makedirs(os.path.join(currentPath,subName),exist_ok=True)
    return os.path.join(currentPath,subName)

def findurl(url,lastDir):
    r=requests.get(url)
    data = bs4.BeautifulSoup(r.text, "html.parser")
    targetPath=createFolder(url,lastDir)
    for l in data.find_all("a"):
        print("current link"+base+l["href"])
        r = requests.get(base + l["href"])
        lastName = r.url.split('/')[-1]
        if lastName.find(".")>0:
            print("this is file ")
            targetname=os.path.join(targetPath,lastName)
            if os.path.exists(targetname):
                pass
            else :
                response=urllib.request.urlretrieve(r.url,targetname)
                
        else:
            print("this is folder name is "+lastName)
            findurl(r.url,targetPath)
    newUrl=''
    return newUrl
print(os.getcwd())
findurl(url,os.getcwd())

print(" everything is downloaded please verify file content and size")