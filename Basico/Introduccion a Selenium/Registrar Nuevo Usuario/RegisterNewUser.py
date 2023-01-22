import unittest
from selenium import webdriver


class RegisterNewUser(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r"C:\Users\lopez\OneDrive - Universidad de Costa Rica\Escritorio\software\chromedriver.exe")
        driver = self.driver        
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get('http://demo-store.seleniumacademy.com/')
    
    def test_new_user(self):
        driver= self.driver
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_partial_link_text('Log In').click()

        create_accout_button= driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span').click()
   
        # self.assertTrue( create_accout_button.is_displayed() and create_accout_button.is_enabled())
        
        self.assertEqual('Create New Customer Account', driver.title)
        
        first_name=driver.find_element_by_id('firstname')
        middle_name=driver.find_element_by_id('middlename')
        last_name=driver.find_element_by_id('lastname')
        email_address=driver.find_element_by_id('email_address')
        news_letter_subscription=driver.find_element_by_id('is_subscribed')
        password=driver.find_element_by_id('password')
        confirm_password=driver.find_element_by_id('confirmation')
        submit_button=driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button')
        
        # self.assertTrue(first_name.is_enable() and last_name.is_enable() and middle_name.is_enable() and email_address.is_enable() and news_letter_subscription.is_enable() and password.is_enable() and confirm_password.is_enable() and submit_button.is_enable() )
        
        first_name.send_keys('Test')
        last_name.send_keys('Test')
        middle_name.send_keys('Test')
        email_address.send_keys('email@email.com')
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        submit_button.click()
        
        
        
    # @classmethod         
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
        
        
if __name__ == "__main__":
	unittest.main(verbosity = 2)