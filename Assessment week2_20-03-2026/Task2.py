from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://automationexercise.com/signup')
wait = WebDriverWait(driver, 10)
search=wait.until(EC.presence_of_element_located((By.NAME, 'name')))
search.send_keys('Monkey')

email=wait.until(EC.presence_of_element_located((By.XPATH,'//input[@data-qa="signup-email"]' )))
email.send_keys('Monkey@gmail.com')


driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()
sleep(2)

wait.until(EC.presence_of_element_located((By.ID, "id_gender1")))
driver.find_element(By.ID, "id_gender1").click()
newsletter = driver.find_element(By.NAME, "newsletter")
offers = driver.find_element(By.NAME, "optin")
newsletter.click()
offers.click()

print("Newsletter selected:", newsletter.get_attribute("checked"))
print("Offers selected:", offers.get_attribute("checked"))
sleep(3)
driver.quit()
