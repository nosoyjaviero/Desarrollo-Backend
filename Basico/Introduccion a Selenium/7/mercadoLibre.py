import unittest
from selenium import webdriver
from time import sleep
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
    

class ExplicitWaitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r"C:\Users\lopez\OneDrive - Universidad de Costa Rica\Escritorio\software\chromedriver.exe")
        driver = self.driver.get('https://mercadolibre.com/')     
        # driver.maximize_window()
        # driver.implicitly_wait(30)
        
    
    def test_acount_link(self):
        driver=self.driver
        country=driver.find_element_by_id('CR').click()
        
        search_field=driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        
        search_field.send_keys('PlayStation 4')
        search_field.submit()
        # sleep(3)
        
        # location= driver.find_element_by_link_text("San José")
        location = driver.find_element_by_xpath('/html/body/main/div/div[2]/aside/section/div[2]/ul/li[1]/a/span[1]')
        
        location.click()
        # sleep(5)
        
        
        condicion= driver.find_element_by_xpath('/html/body/main/div/div[2]/aside/section[2]/div[1]/ul/li[1]/a/span[1]')
        condicion.click()
        # sleep(5)
        
        order_menu=driver.find_element_by_class_name('andes-dropdown__trigger')
        order_menu.click()
        # sleep(5)
        
        higher_price=driver.find_elements_by_xpath('//*[@id="andes-dropdown-mayor-precio-list"]')
        order_menu.click()
        
        articles =[]
        prices=[]
        i=1
        while i!=0:
            
            try:                
                    article_name= driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div[2]/section/ol/li[{i}]/div/div/div[2]/div[1]/a/h2').text
                    
                    articles.append(article_name)
                    
                    article_price=driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div[2]/section/ol/li[{i}]/div/div/div[2]/div[2]/div[1]/div/div/div/div/span[1]/span[2]/span[2]').text
                    prices.append(article_price)
                    
                    
                    
                    
                    
                    
                    i+=1                
            except:
                break
        
        
        print(articles,prices)  
         
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
	unittest.main(verbosity = 2)
 