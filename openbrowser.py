#most important part browser version & jar file version should be same


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome(executable_path="D:\drivers\chromedriver.exe")  #path of the chrome driver

driver.get("https://www.google.com") # getting the URL in the browser

print(driver.title) # getting the title of url
print(driver.current_url) # getting the current url
print(driver.page_source) # getting the HTML page source

driver.close() # closing the focussed  browser after finish code
driver.quit() #close whole the browser