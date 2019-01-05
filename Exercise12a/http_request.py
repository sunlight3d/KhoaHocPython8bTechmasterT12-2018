import urllib.request
import shutil
import tempfile
import json
import re
from xml.dom.minidom import parse, parseString
class HTTPRequest:
    def __init__(self, url):
        self.url = url
        self.file_name = 'output.html'
    def get_response(self):
        with urllib.request.urlopen(self.url) as response:
            self.file = open(self.file_name,"w+")            
            self.text_response = response.read().decode("utf-8")
            self.file.write(self.text_response)            
            self.file.close()                        
            print('aaa')
    def get_objects_from_text(self):
        # self.file = open(self.file_name,'r')
        # self.text_response = self.file.read()
        # self.file.close() 
        matchObj = re.search( r'usd[\s\t\r]*</th>[\s\t\r]*<td>[\s\t\r]*(.*)<div>(.*)[\s\t\r]*(.*)</td>', self.text_response, re.I)
        # matchObj = re.match( r'usd[\s\t\r]*', self.text_response, re.I)
        if matchObj:
            print ("matchObj.group() : ", matchObj.group())
            print ("matchObj.group(1) : ", matchObj.group(1))   
        else:
            print ("No match!!")