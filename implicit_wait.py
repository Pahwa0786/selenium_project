#implicit wait will define only ones
#it will wait for all the elements on the webpage


from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="D:\drivers\chromedriver.exe")

driver.get("https://www.keynotesupport.com/internet/web-contact-form-example-radio-buttons.shtml")
driver.implicitly_wait(10)   #this will wait for all the elements on webpage



element=driver.find_element_by_xpath("/html/body/article/section/div[2]/form/div/span[1]/input")


