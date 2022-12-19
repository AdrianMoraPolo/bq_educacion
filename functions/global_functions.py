import time
import unittest




class globalfunctions():
    def __init__(self,driver):
        self.driver=driver

    def time(self,tie):
        t=time.sleep(tie)
        return t
    def route(self, Url):
        self.driver.get(Url)
        self.driver.maximize_window()