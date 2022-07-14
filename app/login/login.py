from lib2to3.pgen2 import driver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

driver = Chrome()

driver.get('https://www.ups.com/lasso/login')

USERNAME = 'iatoilet'
PASSWORD = 'Il"tmyself123'

email = driver.find_element(By.ID, 'email').send_keys(USERNAME)
input = driver.find_element(By.ID, 'pwd').send_keys(PASSWORD)
submit = driver.find_element(By.ID, 'submitBtn').click()

new_submit = None
try:
    new_submit = driver.find_element(By.ID, 'submitBtn')
except:
    ...

if new_submit:
    print('prehaps credentials are not correct')