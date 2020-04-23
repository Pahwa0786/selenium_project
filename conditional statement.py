from selenium import webdriver
from  selenium.webdriver.common.keys import Keys

import time

driver=webdriver.Chrome(executable_path="D:\drivers\chromedriver.exe")
driver.maximize_window()   #this is for maximize the current window
driver.fullscreen_window()  #this is for fullscreen the current window

driver.get("https://www.keynotesupport.com/internet/web-contact-form-example-radio-buttons.shtml")

element=driver.find_element_by_xpath("/html/body/article/section/div[2]/form/div/span[1]/input")

print(element.is_displayed())   #this is used for checking field is dipyaed or not it will give result in boolean

print(element.is_enabled()) #this is used for checking field is enabled  or not it will give result in boolean

radiobutt=driver.find_element_by_xpath("/html/body/article/section/div[2]/form/div/span[4]/input")

print(radiobutt.is_selected())  #this is used for checking radiobutton is selected  or not it will give result in boolean

driver.quit()