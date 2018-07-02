#code for logging fb account and sending message using selenium python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
usr="eg5287@gmail.com"
pwd="i@eshgupta"
driver = webdriver.Firefox(executable_path="/home/thebrain-eshita/Documents/geckodriver")
driver.get('https://www.facebook.com/')
print ("Opened facebook...")
sleep(1)
a = driver.find_element_by_id('email')
a.send_keys(usr)
print ("Email Id entered...")
sleep(1)
b = driver.find_element_by_id('pass')
b.send_keys(pwd)
print ("Password entered...")
c = driver.find_element_by_id('loginbutton')
c.click()
print ("Done...")
driver.get_screenshot_as_file("/home/thebrain-eshita/Documents/fb1.png")
d = driver.find_element_by_name("q")
d.send_keys("Tejashwa Sharma")
f =driver.find_element_by_class_name("_585_")
f.click()
g =driver.find_element_by_class_name("_6a uiPopover _5tfz openToggler selected")
g.click()
i = driver.find_element_by_class_name("_54nh")
i.click()
j =driver.find_element_by_class_name("_1mf _1mj")
j.send_keys("hello")
k =driver.find_element_by_class_name("_6gd _21u1")
k.click()






