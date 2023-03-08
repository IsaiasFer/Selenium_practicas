import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class HelloWorld(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(executable_path=r'msedgedriver')
        driver = self.driver
        driver.implicitly_wait(10)

    
    def test_hello_world(self):
        driver = self.driver
        driver.get('http://www.platzi.com')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello-world-report'))
