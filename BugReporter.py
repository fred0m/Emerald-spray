import requests

class BugReporter :
    def __init__(self) :
        # 每次写入会覆盖上次的内容
        with open("error.log", mode = 'r', encoding = "utf-8") as error :
            try :
                sender = error.read()
                requests.get("https://sc.ftqq.com/SCU44058T44cff9901b6466371f4ae9be28645f945c57ed47b8bb0.send?text=软件错误报告 & desp="+sender)
                raise Exception("请检查 error.log")
            except : 
                requests.get("https://sc.ftqq.com/SCU44058T44cff9901b6466371f4ae9be28645f945c57ed47b8bb0.send?text=软件错误报告 & desp=未成功获取到错误报告")
                raise Exception("程序异常")
