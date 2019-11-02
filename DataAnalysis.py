from bs4 import BeautifulSoup
import re
from Es import WebGeter
import asyncio

class DataAnalysis :
    def __init__(self, raw_data) :
        self.raw_data = BeautifulSoup(raw_data, features="lxml")
        self.num = len(self.raw_data.findAll(name = "span", attrs = {"class" : "title"}))

    def steam250_dataHandle(self) -> (iter) :
        for i in range(0, self.num) :
            yield {
                "name" : self.raw_data.findAll(name = "span",attrs = {"class":"title"})[i].find(name = "a").string,
                "url" : self.raw_data.findAll(name = "span",attrs = {"class":"title"})[i].find(name = "a")['href'].replace("\n",""),
                "score" : self.raw_data.findAll(name = "span",attrs = {"class":"score"})[i].string
                }

    def steam_dataHandle(self) -> (dict) :
        data = {}
        # 游戏名
        data["Gamename"] = self.raw_data.find("div", class_ = "apphub_AppName").string
        # 开发商
        data["Developer"] = self.raw_data.find("div", class_ = "dev_row").find(name = "a").string
        # 近期评论
        data["Recent Reviews"] = self.raw_data.findAll("div", class_ = "summary column")[0].find("span").string
        # 总体评论
        data['Overall Reviews'] = self.raw_data.find_all("div", class_ = "summary column")[1].find("span").string
        # 介绍
        data['Description'] = re.search(r"(.*)\t(.*\S)", str(self.raw_data.find("div", class_ = "game_description_snippet").string)).groups()[1]
        # 价格
        data['Price'] = re.search(r"(.*)\t(.*\S)", str(self.raw_data.find("div", class_ = "game_purchase_price price").string)).groups()[1]
        # 配置需求
        # 防止没有配置要求
        try :
            try :
                data_ = self.raw_data.find("div", class_ = "game_area_sys_req_full")
                data["Configuration"] = self.load(data_)
            except :
                right_data = self.raw_data.find("div", class_ = "game_area_sys_req_rightCol")
                left_data = self.raw_data.find("div", class_ = "game_area_sys_req_leftCol")
                data["Configuration"] = [self.load(left_data), self.load(right_data)]
        except :
            data["Configuration"] = {}
        # 标签
        data["tag"] = []
        for i in self.raw_data.find_all("a", class_ = "app_tag") :
            data["tag"].append(re.search(r"(.*)\t(.*\S)", str(i.string)).groups()[1])
        return data
    def __load(self, data) :
        about = {}
        for i in data.find_all("li") :
            about[str(re.search(r"strong>(.*?)<", str(i)).groups()[0])] = re.search(r"strong> (.*?)<", str(i)).groups()[0]
        type_ = re.search(r"strong>(.*?)<", str(data)).groups()[0]
        dict = {type_ : about}
        return dict
