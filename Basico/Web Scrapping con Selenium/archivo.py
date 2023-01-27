import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import pandas as pd

website='https://www.adamchoi.co.uk/teamgoals/detailed'
ruta= r"C:\Users\lopez\OneDrive - Universidad de Costa Rica\Escritorio\software\chromedriver.exe"
driver = webdriver.Chrome(ruta)
# open Google Chrome with chromedriver
driver.get(website)

# locate a button
all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
# click on a button
all_matches_button.click()

box = driver.find_element_by_class_name('panel-body')


country = Select(box.find_element_by_id('country'))
country.select_by_visible_text('Spain')

# sleep(20)

matches = driver.find_elements_by_css_selector('tr')
all_matches=[]

for match in matches:
    all_matches.append(match.text)
    # print(match.text)

#  = [match.text for match in matches] #dictionary comprehations

#quit drive we opened in the beginning

driver.quit()

# Bonus: Create Dataframe in Pandas and export to CSV (Excel)
df = pd.DataFrame({'partidos': all_matches})
df.to_csv('./LaLiga.csv', index=False, encoding='utf-8')