#scrapping of a website and storing data in a text file using selenium python

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
path ="/home/thebrain-eshita/Documents/LEGAL/"
driver = webdriver.Firefox(executable_path="/home/thebrain-eshita/Documents/geckodriver")
driver.get("https://www.legalcrystal.com/")
a=driver.find_element_by_id("JudgementName")
a.send_keys("State of Orissa vs Ram Bahadur Thapa (1959) ")
a.submit()
time.sleep(10)
i=0
p=0

def writing(p):
    i=p
    heading = len(driver.find_elements_by_xpath("//h4[@class='title media-heading']/a"))
    for head in range(heading):
      driver.find_elements_by_xpath("//h4[@class='title media-heading']/a")[head].click()
      time.sleep(5)
      data = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[2]/div/div/table[3]")
      time.sleep(5)
      data =data.text
      file = open (path + str(i) +".txt","w")
      file.write(data)
      i=i+1
      driver.back()
      return i


for a in range(60):
    p=writing(p)
    next = driver.find_element_by_xpath("//li[@class='next']/a")
    next.click()
