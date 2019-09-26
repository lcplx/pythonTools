import requests,urllib,urllib.request,bs4,os,shutil
from datetime import datetime
from bs4 import BeautifulSoup
from ProMetaData import findurl
from pro7zprocess import extract7z



urlProduct="http://10.92.99.111:50000/csiroot/cservlet/DownloadLog?zip=1&file=/usr/sap/FSPRO/ps/product"
urlApp="http://10.92.99.111:50000/csiroot/cservlet/DownloadLog?zip=1&file=/usr/sap/FSPRO///ps/metadata/xml/app_tables"
urlDataObj="http://10.92.99.111:50000/csiroot/cservlet/DownloadLog?zip=1&file=/usr/sap/FSPRO///ps/metadata/xml//data_objects"
targetApptable="C:/Users/liangx/Desktop/Documents/PythonTool/download/app_tables"
targetDataOBject="C:/Users/liangx/Desktop/Documents/PythonTool/download/data_objects"
targetProduct="C:/Users/liangx/Desktop/Documents/PythonTool/download/product"
base='http://10.92.99.111:50000/csiroot/cservlet/'
workingAppFld="C:/Projects/eastwestageas/FS-QUO-toolkit-400.1.0/FS-QUO-dev/target/home/ps/metadata/xml/app_tables"
workingdataOFld="C:/Projects/eastwestageas/FS-QUO-toolkit-400.1.0/FS-QUO-dev/target/home/ps/metadata/xml/data_objects"
workingProdFld="C:/Projects/eastwestageas/FS-QUO-toolkit-400.1.0/FS-QUO-dev/target/home/ps/product"

targetTime=datetime(2019,9,23,hour=0,minute=00)


def checkNewJar(item):
    for x in item:
        ts=x.contents[0]
        x=datetime.strptime(ts,"%Y-%m-%d %H:%M:%S.%f")
        return targetTime<x

def downloadzip(url,targetfld,targetTime):
    os.makedirs(targetfld,exist_ok=True)
    r=requests.get(url)
    data = bs4.BeautifulSoup(r.text, "html.parser")
    for tr in data.find_all("tr"):
        tds=tr.find_all("td")
        # print(type(tds))
        item = tds[1:2]
        isnewJar=checkNewJar(item)
        link=tds[0:1]
        if isnewJar:
            for l in link:
                url=l.contents[0]
                # print(url["href"])
                print(base+url["href"])
                r = requests.get(base+url["href"])
                lastName = r.url.split('/')[-1]
                targetname=os.path.join(targetfld,lastName)
                response=urllib.request.urlretrieve(r.url,targetname+".zip")
                print(targetname+"get downloaded ")

shutil.rmtree(targetApptable,True)
shutil.rmtree(targetDataOBject,True)
shutil.rmtree(targetProduct,True)
downloadzip(urlApp,targetApptable,targetTime)
downloadzip(urlDataObj,targetDataOBject,targetTime)
downloadzip(urlProduct,targetProduct,targetTime)
extract7z(targetApptable,workingAppFld)
extract7z(targetDataOBject,workingdataOFld)
extract7z(targetProduct,workingProdFld)



