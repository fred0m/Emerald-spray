from Es import WebGeter
from Es import DataAnalysis

class es :
    def __init__(self, url) :
        self.url = url
        self.html = ""
        self.__html()

    def __html(self) :
        self.html = WebGeter(self.url).raw_html
    
    def steam(self) -> (dict) :
        return DataAnalysis(self.html).steam_dataHandle()

    def steam250(self) -> (iter) :
        return DataAnalysis(self.html).steam250_dataHandle()

