import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By #pip3 install webdriver-manager

class AssertionsTest(unittest.TestCase):
   
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r"C:\Users\lopez\OneDrive - Universidad de Costa Rica\Escritorio\software\chromedriver.exe")
        driver = self.driver  
        # driver.implicitly_wait(30)      
        # driver.maximize_window()        
        driver.get('http://demo-store.seleniumacademy.com/')
        
    def test_search_field(self):
        # self.assertTrue(self.is_element_present( By.NAME, "q" )) #new api selenium
        self.assertTrue(self.driver.find_element_by_name('q')) #old api selenium
        
    
    def test_language_option(self):    
      # self.assertTrue( self.is_element_present(By.ID, "select-language" )) #new api selenium
      self.assertTrue(self.driver.find_element_by_id("select-language" )) #old api selenium
        
    #is_element  es una funcion de utilidad  para  identificar cuando un elemnto esta presente de acuerdo a esto parametros
    #how, el tipo de selector
    #what, el valor que tiene
    #
    # def is_element_present (self,how, what):
    #     try:
    #       self.driver.find_element(by =how, value =what)
    #     except NoSuchElementException as var:
    #       return False
     
 
        
    # @classmethod         
    def tearDown(self):
        self.driver.quit()
    
if __name__ == "__main__":
	unittest.main(verbosity = 2)
 
 