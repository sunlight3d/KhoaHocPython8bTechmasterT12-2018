import urllib.request
import shutil
import tempfile
import json
import re
from xml.dom.minidom import parse, parseString
from database_manager import DatabaseManager

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.chrome.service as service
from webdriver_manager.chrome import ChromeDriverManager

import time

class HTTPRequest:
    def __init__(self, url):
        self.url = url
        self.file_name = 'output.html'
    def get_response(self):
        # response = urllib.request.urlopen(self.url,timeout=10)
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(self.url)        
        self.file = open(self.file_name,"w")            
        # self.text_response = response.read().decode("utf-8")        
        time.sleep(3)
        self.text_response = driver.page_source
        self.file.write(driver.page_source)            
        self.file.close()            
                          
    def get_objects_from_text(self):
        self.file = open(self.file_name,'r')
        self.text_response = self.file.read()
        self.file.close() 
        rows = re.findall( r'([a-zA-Z]{3})[\s\t\r]*</th>[\s\t\r]*<td>[\s\t\r]*([\d\,]*)<div>([\d\,]*)<div>([\d\,]*)[\s\t\r]*</div>', self.text_response, re.MULTILINE|re.I)                
        for row in rows:            
            name = row[0]
            muaTM = float(row[1].replace(',','.'))
            muaCK = float(row[2].replace(',','.'))
            ban = float(row[3].replace(',','.'))
            try:
                DatabaseManager.get_instance().insert_into_exchanges(name,muaTM, muaCK,ban)
            except Exception as ex:
                pass                            
            