import aiohttp
import asyncio

class WebGeter : 
    def __init__(self, url) :
        self.url = url
        self.head = {
                "User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
                "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language" : "zh-CN",
                "Connection" : "keep-alive",
                "Accept-Charset" : "utf-8;q=0.7,*;q=0.7"
                }
        self.raw_html = ""
        self.__loop()

    async def getRawData(self) :
            async with aiohttp.ClientSession() as session :
                async with session.get(self.url, headers = self.head) as response :
                    self.raw_html = await response.text()
        
    def __loop(self) :
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        task = [self.getRawData()]
        loop.run_until_complete(asyncio.wait(task))
        loop.close()

