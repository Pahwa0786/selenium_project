#find how many links present in web page
#print all the links
#click on the links

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome(executable_path="D:\drivers\chromedriver.exe")
driver.get("https://makemytrip.com")
driver.maximize_window()
#getting the count of all the links
links=driver.find_elements(By.TAG_NAME,'a')
print(len(links))

#printing all the links
for link in links:
    print(link.text)
time.sleep(5)

#clicking on the links
#driver.find_element(By.LINK_TEXT,'Holidays').click()

driver.find_element(By.PARTIAL_LINK_TEXT,'Hol').click()
