#code for creating a facebook account using python and selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
firstname = "Eshii"
lastname  = "raichand"
phone = "8962104224"
driver = webdriver.Firefox(executable_path="/home/thebrain-eshita/Documents/geckodriver")
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/")
a = driver.find_element_by_name("firstname")
a.send_keys(firstname)
b = driver.find_element_by_name("lastname")
b.send_keys(lastname)
c = driver.find_element_by_name("reg_email__")
c.send_keys(phone)
d = driver.find_element_by_name("reg_passwd__")
d.send_keys("Ia23@_5")
e =driver.find_element_by_id('day')
e.click()
sleep(3)
e.send_keys("28")
f2 = driver.find_element_by_id("month")
f2.click()
sleep(3)
f2.send_keys("Jun")
g =driver.find_element_by_id("year")
g.click()
sleep(3)
g.send_keys("1997")
driver.find_element_by_css_selector("input[type = 'radio'][value = '1']").click()
h = driver.find_element_by_name("websubmit")
sleep(10)
h.click()
