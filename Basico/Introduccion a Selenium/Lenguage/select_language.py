import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
class LanguageOptions(unittest.TestCase):
   
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r"C:\Users\lopez\OneDrive - Universidad de Costa Rica\Escritorio\software\chromedriver.exe")
        driver = self.driver        
        # driver.maximize_window()
        # driver.implicitly_wait(30)
        driver.get('http://demo-store.seleniumacademy.com/')
    
    def test_select_language(self):
        exp_options = ['English', 'French','German']
        act_options= []
        select_language= Select(self.driver.find_element_by_id('select-language'))
        self.assertEqual(3,len(select_language.options))
        for option in select_language.options:
            act_options.append(option.text)
        self.assertListEqual(exp_options,act_options)
        
        self.assertEqual('English', select_language.first_selected_option.text)
        
        select_language.select_by_visible_text('German')
        
        self.assertTrue('store=german' in self.driver.current_url )
        self.driver.implicitly_wait(20)
        select_language= Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)
        
        
    def tearDown(self):
        self.driver.implicitly_wait(20)
        self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)