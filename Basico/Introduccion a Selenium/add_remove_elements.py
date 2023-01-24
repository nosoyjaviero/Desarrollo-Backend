import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):
  
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r"C:\Users\lopez\OneDrive - Universidad de Costa Rica\Escritorio\software\chromedriver.exe")
        driver = self.driver        
        # driver.maximize_window()
        
        driver.get('https://the-internet.herokuapp.com/')
        driver.implicitly_wait(30)
        driver.find_element_by_link_text('Add/Remove Elements').click()
    
    def test_add_remove(self):  
        driver=self.driver      
        elements_added= int(input('How many elements will you ad?: '))
        elements_removed=  int(input('How many elements will you remove?: '))
        total_elements= elements_added-elements_removed
        
        add_button= driver.find_element_by_xpath('//*[@id="content"]/div/button')
        sleep(3)
        for i in range(elements_added):
            add_button.click()
        
        for i in range(elements_removed):
            try:
                delete_button=self.driver.find_element_by_xpath('//*[@id="elements"]/button[1]')
                delete_button.click()
            except :
              print('You trying to delete more elements the existent')
              break
          
        if total_elements>0:
            print(f"There are {total_elements} elements on screnn")
        else:
            print("There 0 are elemets on screen")
        sleep(3)
        
        
    def tearDown(self):
        self.driver.close()
    
if __name__ == "__main__":
	unittest.main(verbosity = 2)
 