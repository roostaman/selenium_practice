from selenium import webdriver
from selenium.webdriver.common.by import By

# keep chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"price: {price_dollar}.{price_cent}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("role"))

# button = driver.find_element(By.ID, value="submit")
# print(button.get_attribute("class"))
# print(button.size)


driver.quit()
