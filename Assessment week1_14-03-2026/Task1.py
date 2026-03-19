from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = opts)
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
sleep(2)
print("Web Browser Opened")

# 1
username = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
print(username)
print("Username field found")

# 2
password = driver.find_element(By.CSS_SELECTOR, 'input[id="password"]')
print(password)
print("Password field found")

# 3
login_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
print(login_btn)
print("Login button found")

# 4
footer = driver.find_element(By.CSS_SELECTOR,'div[style = "text-align: center;"] a')
print(footer.text)
print("Elemental Selenium link found")

sleep(3)

driver.quit()