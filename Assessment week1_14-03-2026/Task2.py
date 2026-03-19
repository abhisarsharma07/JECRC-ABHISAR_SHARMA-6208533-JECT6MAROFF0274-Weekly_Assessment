from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = opts)

# 1
driver.get("https://www.wikipedia.org/")
driver.maximize_window()
sleep(2)
print("Wikipedia open")

# 2
search = driver.find_element(By.ID, "searchInput")
print(search)
print("Search input field found")

# 3
english = driver.find_element(By.ID, "js-link-box-en")
print(english)
print("English language link found")

# 4
logo = driver.find_element(By.CLASS_NAME, "central-featured-logo")
print(logo)
print("Wikipedia logo found")

# 5
languages = driver.find_elements(By.CSS_SELECTOR, ".central-featured a")
print(languages)
print(len(languages))
print("Total language links found")
sleep(2)

# 6
driver.back()
print("Navigated back")
sleep(2)

# 7
driver.forward()
print("Navigated forward")
sleep(2)

# 8
driver.refresh()
print("Page refreshed")
sleep(2)

# 9
print("Final Page Title:", driver.title)

# 10
driver.quit()