#encoding=utf-8
#---------------------------------------------------------------------------------------------------
#Copyright: Copyright (c) 2019
#Created on 2019-10-08
#Author:fredom
#Version 1.0
#---------------------------------------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup
from BugReporter import BugReporter
import os

class WebGeter :

    def __init__(self,inputUrl) :
            self.url = inputUrl
            self.getRawData()

    def getRawData(self):
        headers={"User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
                 "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                 "Accept-Language" : "zh-CN",
                 "Connection" : "keep-alive",
                 "Accept-Charset" : "utf-8;q=0.7,*;q=0.7"}

        try: #异常处理机制
            r = requests.get(self.url,timeout=30,headers=headers,allow_redirects=False)
            r.raise_for_status()#监视错误信息
            r.encoding = "utf-8"
            self.raw_data = r.text
            self.raw_data =  BeautifulSoup(self.raw_data,"html.parser")
        except:
            if (os.path.exists("error.log")):#异常处理报警方案
                BugReporter()
            else:
                pass
            with open("error.log","a") as f :
                f.write("errorcode:1001"+"\n\n"+"time:"+str(time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time())))+"\n\n"+"pwd:"+str(os.getcwd())+"\n")
                BugReporter()

if __name__ == '__main__':
    main = WebGeter()
