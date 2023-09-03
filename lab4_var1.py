

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from urllib.parse import urlparse
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class TestPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
       

    def test_url_are_clickable(self):
        driver = self.driver
        driver.get("https://www.selenium.dev/blog/")
        n = len(driver.find_elements(By.XPATH, "//a[@class='selenium-link']"))
        for i in range(0,n):
            time.sleep(2)
            open_url = driver.find_elements(By.XPATH, "//a[@class='selenium-link']")[i]
            ActionChains(driver).key_down(Keys.CONTROL).click(open_url).key_up(Keys.CONTROL).perform()
        print()
        print()
        print()
        print("Количество статей на гланой страннице :",n)
    
    def test_pages_are_clickable(self):
        driver = self.driver
        driver.get("https://www.selenium.dev/blog/")
        m =  len(driver.find_elements(By.XPATH, "//a[@class='page-link']")) 
        for k in range(3,m):
            time.sleep(2)
            pagination = driver.find_elements(By.XPATH, "//a[@class='page-link']")[k]
            ActionChains(driver).key_down(Keys.CONTROL).click(pagination).key_up(Keys.CONTROL).perform()
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

