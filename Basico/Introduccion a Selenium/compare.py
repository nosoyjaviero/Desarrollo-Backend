import unittest
from selenium import webdriver

class CompareProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r"C:\Users\lopez\OneDrive - Universidad de Costa Rica\Escritorio\software\chromedriver.exe")
        driver = self.driver        
        # driver.maximize_window()
        # driver.implicitly_wait(30)
        driver.get('http://demo-store.seleniumacademy.com/')
        
    def test_compare_prooducts_remocal_alert(self):
        driver= self.driver
        
        #seleccionamos la busqueda
        search_field=driver.find_element_by_name('q')
        search_field.clear()
        
        #esto va a hacer que aparecezcan los resultados de busqueda y la realizamos
        search_field.send_keys('tee')
        search_field.submit()
        
        #buscamos el elemento para comparar
        driver.find_element_by_class_name('link-compare').click()
        #Limpiamos los elementos agregados al carrito
        driver.find_element_by_link_text('Clear All').click()
        # alert=driver.switch_to_alert()
        alert = driver.switch_to.alert
        # alert.accept()
        alert_text= alert.text
        self.assertEqual('Are you sure you would like to remove all products from your comparison?',alert_text)
        
        alert.accept()
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)