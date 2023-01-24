import unittest
from selenium import webdriver
from time import sleep

class Tables(unittest.TestCase):
  
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r"C:\Users\lopez\OneDrive - Universidad de Costa Rica\Escritorio\software\chromedriver.exe")
        driver = self.driver        
        # driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Sortable Data Tables').click()
    
    def test_sort_tables(self):
            driver=self.driver
            table_data=[[]for i in range(5) ]
            print(table_data)
            
            for i in range(1,5):
                header=driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i}]/span')
                table_data[i].append(header.text)
                
                for j in range(1,6):
                    
                    row_data=driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{i}]/td[{j}]')
                   
                    table_data[i].append(row_data.text)
                    
            print(table_data)
            
            
    
        
        
    def tearDown(self):
        self.driver.close()
    
if __name__ == "__main__":
	unittest.main(verbosity = 2)
 