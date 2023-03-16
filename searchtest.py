import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class SearchTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(executable_path=r'msedgedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.get('http://demo-store.seleniumacademy.com')

    def test_search_tee(self):
        """ Buscando searchBox de nombre 'q' y escribiendo tee en el para buscarlo """
        driver = self.driver
        search_field = driver.find_element('name', 'q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

    def test_search_shaker(self):
        """ Buscando searchBox de nombre 'q' y escribiendo salt shaker para buscarlo """
        driver = self.driver
        search_field = driver.find_element('name', 'q')
        search_field.clear()

        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements(
            'xpath', '//*[@id="product-collection-image-389"]')
        self.assertEqual(1, len(products))

    def tearDown(self):
        self.driver.quit()
