#navigate from one url to another


from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import  time   #importing time
driver=webdriver.Chrome(executable_path="D:\drivers\chromedriver.exe")

driver.get("https://www.google.com")   #getting the URL
print(driver.title)
time.sleep(2)  # giving sleep time in secs
driver.get("https://fb.com")   #getting next url

print(driver.title)
time.sleep(2)

driver.back()  #back action using browser button
time.sleep(2)
driver.forward() #forward action using browser button
time.sleep(2)
driver.refresh()   #refresh the current url
driver.quit()