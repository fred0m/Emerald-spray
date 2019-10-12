import requests
from bs4 import BeautifulSoup
import time
from .BugReporter import BugReporter

class WebGeter :
    def __init__(self, inputUrl) :
        self.url = inputUrl
        # 将参数绑定 拒绝魔法值 方便代码管理
        self.head = {
                    "User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
                    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Accept-Language" : "zh-CN",
                    "Connection" : "keep-alive",
                    "Accept-Charset" : "utf-8;q=0.7,*;q=0.7"
                }
        self.getRawData()

    def getRawData(self) :
        try :
            r = requests.get(self.url,timeout=30,headers=self.head,allow_redirects=False)
            r.raise_for_status()
            r.encoding = "utf-8"
            self.raw_data = r.text
            # self.raw_data =  BeautifulSoup(self.raw_data,"html.parser")
            # lxml 解析速度最快
            try :
                self.raw_data =  BeautifulSoup(self.raw_data,"lxml")
            # 如果没有 lxml ,则使用 bs4 自带的 html.parser
            except :
                self.raw_data =  BeautifulSoup(self.raw_data,"html.parser")
        # 获取错误信息 
        # Exception 是所有错误信息的父类
        except Exception as e :
            # 若目录下没有 error.log 
            # with open 会自动创建
            with open("error.log", "w") as f :
                # f.write("errorcode:1001"+"\n\n"+"time:"+str(time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time())))+"\n\n"+"pwd:"+str(os.getcwd())+"\n")
                # 使代码更可读
                # \ 表示连接
                f.write("errorcode:1001" + "\n\n"
                        "time:" + str(time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time())))+ "\n\n"
                        "raise : " + str(e))
                BugReporter()
