import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssersionsTest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Edge(executable_path=r'msedgedriver')
        driver=self.driver
        driver.implicity_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_search_language_selector(self):
        self.assertTrue(self.is_element_present(By.ID, 'language_selector'))

    def tearDown(self):
        self.driver.quit()

    def is_element_present(self,how,what):
        try:
            self.driver.element(by=how, value=what)
        except NoSuchElementException as variable:
            return False
        return True

if __name__=='__main__':
    unittest.main(verbosity=2)
