import requests,urllib,urllib.request,bs4,os
from bs4 import BeautifulSoup
import zipfile,logging
url='http://10.92.99.111:50000/csiroot/cservlet/DownloadLog?zip=1&file=/usr/sap/FSPRO//ppms/app//runtime/xml//app_tables/app_tables_100_2.5.0.xml'
base='http://10.92.99.111:50000/csiroot/cservlet/'

logging.basicConfig(filename='download.log',level=logging.DEBUG)
urllib.request.urlretrieve(url,"123.xml")

with zipfile.ZipFile('123.xml','r') as zui:
    zui.extractall()


