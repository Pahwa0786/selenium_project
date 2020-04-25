from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="D:\drivers\chromedriver.exe")

driver.get("https://www.expedia.com")

driver.implicitly_wait(10)

driver.find_element_by_xpath("/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]/section[2]/form/div[6]/div/div/div[1]/label/input").send_keys("chandigarh")
driver.find_element_by_xpath("/html/body").send_keys("04/24/2020")

driver.find_element(By.ID("hotel-checkout-hp-hotel")).send_keys("04/25/2020")
driver.find_element_by_xpath("/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]/section[2]/form/div[13]/label/button").click()