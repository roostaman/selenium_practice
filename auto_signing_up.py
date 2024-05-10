from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://secure-retreat-92358.herokuapp.com/")

name_bar = driver.find_element(By.NAME, value="fName")
last_name_bar = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

name_bar.send_keys("Rustam")
last_name_bar.send_keys("Akhmet")
email.send_keys("smmzver@gmail.com")

signup_button = driver.find_element(By.XPATH, value="//button[@type='submit']")
signup_button.click()
