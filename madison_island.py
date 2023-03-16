import unittest 
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class MadisonIsland(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Edge(executable_path=r'msedgedriver')
        driver=self.driver
        driver.get('https://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        

    def test_madison_island(self):
        """ Buscando un elemento con id llamado search """
        search_field=self.driver.find_element('id','search')

    def test_search_text_field_by_name(self):
        """ Buscando un elemento con un name q """
        search_field=self.driver.find_element('name','q')

    def test_search_text_field_by_className(self):
        """ Buscando un elemento con una clase input-text """
        search_field=self.driver.find_element('class name','input-text')
    
    def testSearchButton_enabled(self):
        """ Verificando si un boton está disponible """
        search_field=self.driver.find_element('class name','button')

    def test_zcountOfPromo(self):
        """ Contando cuantas imagenes promocionales hay """
        banner_container=self.driver.find_element('class name',"promos")
        banners=banner_container.find_elements('tag name','img')
        self.assertEqual(3, len(banners))

    def test_vipPromo(self):
        """ Buscando contenido via xPath """
        vip_image=self.driver.find_element('xpath','//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/ul/li[2]/a/img')
    
    def test_ShoppingCart(self):
        """ Buscando icono de carrito """
        carrito=self.driver.find_element('css selector','div.header-minicart span.icon')

    def TearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='madison_island_report'))