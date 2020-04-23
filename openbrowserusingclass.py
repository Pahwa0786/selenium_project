from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class new:

    def chromebrowser(self):
         global driver

         driver=webdriver.Chrome(executable_path="D:\drivers\chromedriver.exe")
         driver.get("https://google.com")

w=new()

w.chromebrowser()


