from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import  time

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="D:\drivers\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()
#how to get how many fields at=re available in a webpage

imputboxes=driver.find_elements(By.CLASS_NAME,'text_field')

print(len(imputboxes))

#send values in fields

driver.find_element(By.ID,'RESULT_TextField-1').send_keys("Himanshu")
driver.find_element(By.ID,'RESULT_TextField-2').send_keys("pahwa")
driver.find_element(By.ID,'RESULT_TextField-3').send_keys("7889171507")
driver.find_element(By.ID,'RESULT_TextField-4').send_keys("India")
driver.find_element(By.ID,'RESULT_TextField-5').send_keys("Rohtak")
driver.find_element(By.ID,'RESULT_TextField-6').send_keys("himanshu.pahwa0786@gmail.com")
#select radiobuttons
driver.find_element(By.XPATH,'/html/body/form/div[2]/div[15]/table/tbody/tr[1]/td/label').click()

#select checkboxes

driver.find_element(By.XPATH,'/html/body/form/div[2]/div[17]/table/tbody/tr[1]/td/label').click()
driver.find_element(By.XPATH,'/html/body/form/div[2]/div[17]/table/tbody/tr[4]/td').click()

#selecting the option from dropdown using different approaches

element=driver.find_element_by_id("RESULT_RadioButton-9")
drp=Select(element)
#drp.select_by_visible_text('Afternoon')
#drp.select_by_index(1)
drp.select_by_value("Radio-2")

#getting how many elements under dropdown

print(len(drp.options))

#capture all the elments & print it

options=drp.options
for a in options:
    print(a.text)