from bs4 import BeautifulSoup
from .WebGeter import WebGeter
from .BugReporter import BugReporter
import time
import re
import json

class steam250URLGeter :
    def __init__(self, raw_data) :
        self.raw_data = raw_data
        # 方便代码管理 避免魔法值
        self.num = len(self.raw_data.findAll(name = "span",attrs = {"class":"title"}))
        # self.data = [] 可以用迭代器 加快程序运行速度
        # self.dataHandle() 

    def dataHandle(self) :
        for i in range(0, self.num) :
            # self.data.append([self.raw_data.findAll(name = "span",attrs = {"class":"title"})[i].find(name = "a").string,self.raw_data.findAll(name = "span",attrs = {"class":"title"})[i].find(name = "a")['href'].replace("\n",""),self.raw_data.findAll(name = "span",attrs = {"class":"score"})[i].string])#0.名字 1.url 2.评分
            # 迭代器关键字 
            # 表示这个函数是一个迭代器
            # 使代码更可读
            yield {
                    "name" : self.raw_data.findAll(name = "span",attrs = {"class":"title"})[i].find(name = "a").string,
                    "url" : self.raw_data.findAll(name = "span",attrs = {"class":"title"})[i].find(name = "a")['href'].replace("\n",""),
                    "score" : self.raw_data.findAll(name = "span",attrs = {"class":"score"})[i].string
            }
    def outputData(self) :
        # 创建迭代器
        # 只能迭代一次
        iter = self.dataHandle()
        nowtime = str(time.strftime('%Y-%m-%d-%H.%M.%S',time.localtime(time.time())))
        with open(nowtime + ".xuan2", "a",encoding='utf-8') as outfile :
            for i in range(int(input("请输入分析个数, 最大为{}>".format(self.num)))):
                data = iter.__next__()
                outfile.write(
                        "name : " + data["name"] + "\n" \
                        "url : " + data["url"] + "\n" \
                        "score : " + data["score"] + "\n"
                        )
                # outfile.write(self.data[i][0]+"\n")
                # outfile.write(self.data[i][1]+"\n")
                # outfile.write(self.data[i][2]+"\n")
    
class detailsDataGeter :
    def __init__(self, url) :
        self.url = url
        self.raw_data = WebGeter(self.url).raw_data
        self.data = {}

    def detailsGeter(self) :
        # 游戏名
        self.data["Gamename"] = self.raw_data.find("div", class_ = "apphub_AppName").string
        # 开发商
        self.data["Developer"] = self.raw_data.find("div", class_ = "dev_row").find(name = "a").string
        # 近期评论
        self.data["Recent Reviews"] = self.raw_data.findAll("div", class_ = "summary column")[0].find("span").string
        # 总体评论
        self.data['Overall Reviews'] = self.raw_data.find_all("div", class_ = "summary column")[1].find("span").string
        # 介绍
        self.data['Description'] = re.search(r"(.*)\t(.*\S)", str(self.raw_data.find("div", class_ = "game_description_snippet").string)).groups()[1]
        # 价格
        self.data['Price'] = re.search(r"(.*)\t(.*\S)", str(self.raw_data.find("div", class_ = "game_purchase_price price").string)).groups()[1]
        # 配置需求
        # 防止没有配置要求
        try :
            try :
                data = self.raw_data.find("div", class_ = "game_area_sys_req_full")
                self.data["Configuration"] = self.load(data)
            except :
                right_data = self.raw_data.find("div", class_ = "game_area_sys_req_rightCol")
                left_data = self.raw_data.find("div", class_ = "game_area_sys_req_leftCol")
                self.data["Configuration"] = [self.load(left_data), self.load(right_data)]
        except :
            self.data["Configuration"] = {}
        # 标签
        self.data["tag"] = []
        for i in self.raw_data.find_all("a", class_ = "app_tag") :
            self.data["tag"].append(re.search(r"(.*)\t(.*\S)", str(i.string)).groups()[1])
        return self.data
   
    def outputData(self) :
        with open("a.json", "w") as text :
            json.dump(self.detailsGeter(), text)

    def load(self, data) :
        about = {}
        for i in data.find_all("li") :
            about[str(re.search(r"strong>(.*?)<", str(i)).groups()[0])] = re.search(r"strong> (.*?)<", str(i)).groups()[0]
        type_ = re.search(r"strong>(.*?)<", str(data)).groups()[0]
        dict = {type_ : about}
        return dict

if __name__ == "__main__" :
    detailsDataGeter("https://store.steampowered.com/app/427520/Factorio/?curator_clanid=32686107").outputData()
    steam250URLGeter(WebGeter("https://steam250.com/").raw_data).outputData()
