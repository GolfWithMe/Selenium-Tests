import unittest
from selenium import webdriver
#from selenium.webdriver.common.keys import keys

driver = webdriver.Firefox()

driver.get("http://dev.golfwithme.biz")

logoutButton = driver.find_elements_by_class_name("dropdown-toggle")
loginName = driver.find_element_by_name("username")
loginPassword = driver.find_element_by_name("password")
loginButton = driver.find_element_by_name("Submit")



#if logoutButton


driver.quit()
