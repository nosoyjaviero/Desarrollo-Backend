import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class DynamicControls(unittest.TestCase):
  
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r"C:\Users\lopez\OneDrive - Universidad de Costa Rica\Escritorio\software\chromedriver.exe")
        driver = self.driver        
        # driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com')
        driver.find_element_by_link_text('Dynamic Controls').click()
    
    def test_dynamic_controls(self):
        driver=self.driver
         
        checkbox=driver.find_element_by_css_selector("#checkbox > input[type=checkbox]")
        checkbox.click()   
        remove_add_button= driver.find_element_by_css_selector("#checkbox-example > button")
        remove_add_button.click()
        
        WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#checkbox-example > button")))
        remove_add_button.click()
        
        enable_disable_button=driver.find_element_by_css_selector('#input-example > button')
        enable_disable_button.click()
        WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#input-example > button')))
        text_area=driver.find_element_by_css_selector('#input-example > input[type=text]')
        text_area.send_keys('platzi')
        enable_disable_button.click()
        sleep(30)
        
        
    def tearDown(self):
        self.driver.close()
    
if __name__ == "__main__":
	unittest.main(verbosity = 2)