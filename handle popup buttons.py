from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Chrome(executable_path="D:\drivers\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/button").click()
time.sleep(5)
#driver.switch_to_alert().accept()
driver.switch_to.alert.dismiss()