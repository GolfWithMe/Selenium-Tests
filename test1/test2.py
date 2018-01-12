import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestGroupActions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    #def tearDown(self):
        #self.driver.quit()

    def test_100(self):
        driver = self.driver
        driver.get("http://dev.golfwithme.biz")

        logoutButton = driver.find_elements_by_class_name("dropdown-toggle")
        loginName = driver.find_element_by_name("username")
        loginPassword = driver.find_element_by_name("password")
        loginButton = driver.find_element_by_name("Submit")

        loginName.send_keys("mikie")
        loginPassword.send_keys("1qaz2wsx#EDC")
        loginButton.click()

        driver.get("http://dev.golfwithme.biz/index.php?option=com_community&view=groupschedule&task=newrequest&Itemid=132")

        groupName = Select(driver.find_element_by_name("selgroup"))
        groupName.select_by_visible_text("Beaver Creek Country Club")

        groupNameField = driver.find_element_by_name("selgroup")

        groupNameField.submit()

        selectList = Select(driver.find_element_by_name("selmember[]"))
        selectList.select_by_visible_text("Mike Myers")
        selectList.select_by_visible_text("test me")
        selectList.select_by_visible_text("mikie3")

        selectListField = driver.find_element_by_id("selmember")

        #selectListField.submit()




if __name__ == '__main__':
    unittest.main()