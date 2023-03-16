import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionsTests(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Edge(executable_path=r'msedgedriver')
        driver=self.driver
        driver.implicitly_wait(30)
        driver.get('http://demo-store.seleniumacademy.com')

    def test_search_field(self):
        """ Buscando elemento de nombre 'q' """
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_search_language_selector(self):
        """ Buscando cambiador de idiomas """
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))

    def is_element_present(self,how,what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as variable:
            return False
        return True

    def tearDown(self):
            self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)
