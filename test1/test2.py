import unittest
from selenium import webdriver
#from selenium.webdriver.common.keys import keys

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


if __name__ == '__main__':
    unittest.main()