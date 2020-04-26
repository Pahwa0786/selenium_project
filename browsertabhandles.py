from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Chrome(executable_path="D:\drivers\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()
driver.find_element_by_xpath("/html/body/footer/div/div/div[2]/a[1]").click()
print(driver.current_window_handle) #CDwindow-A93D1E547E4F20774CFBC2CC325D0245 current window values

handles=driver.window_handles    #handles to other window tab

for handle in handles:
    driver.switch_to_window(handle)
    print(driver.title)