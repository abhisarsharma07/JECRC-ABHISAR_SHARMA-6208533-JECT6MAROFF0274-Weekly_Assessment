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


driver.get('https://www.amazon.in/')
# title=driver.title
# print("Title: ",title)
url = driver.current_url
print("Current URL:", url)

#Locate the category dropdown (next to search bar)
wait=WebDriverWait(driver,10)
dropdown= wait.until(EC.presence_of_element_located((By.XPATH,'//select[@id="searchDropdownBox"]')))
select = Select(dropdown)
select.select_by_visible_text('Books')


search=wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="twotabsearchtextbox"]')))
search.send_keys('Harry Potter', Keys.ENTER)


wait.until(EC.presence_of_all_elements_located((By.XPATH, "//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal']")))

product=driver.find_elements(By.XPATH, '//h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"]/span')



for i in range(5):
    print(product[i].text)

product=driver.find_element(By.XPATH, '//h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"]/span')
product.click()

sleep(5)
driver.quit()