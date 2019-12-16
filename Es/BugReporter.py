#encoding=utf-8
#---------------------------------------------------------------------------------------------------
#Copyright: Copyright (c) 2019
#Created on 2019-10-08
#Author: fredom
#Version 2.0.1
#---------------------------------------------------------------------------------------------------
import requests
import os
import sys
class BugReporter :
    def __init__(self) :
        if (os.path.exists('error.log')):
            errorlog = open ('error.log' , mode = 'r' , encoding = "utf-8")
            sender = errorlog.read()
            requests.get("https://sc.ftqq.com/SCU44058T44cff9901b6466371f4ae9be28645f945c57ed47b8bb0.send?text=软件错误报告 & desp="+sender)
            errorlog.close()
            os.remove("error.log")
            quit()
        else :
            requests.get("https://sc.ftqq.com/SCU44058T44cff9901b6466371f4ae9be28645f945c57ed47b8bb0.send?text=软件错误报告 & desp=未成功获取到错误报告")
            quit()
