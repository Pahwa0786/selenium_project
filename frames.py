from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Chrome(executable_path="D:\drivers\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/")
driver.maximize_window()

#driver.switch_to.frame("packageListFrame")  #swithicg to frame
time.sleep(5)
#driver.find_element_by_xpath("/html/body/div[2]/ul/li[1]/a").click()
#driver.switch_to.default_content() #go back to main content

driver.switch_to.frame("packageFrame")
driver.find_element_by_xpath("/html/body/div/ul/li[11]/a/span").click()
driver.quit()