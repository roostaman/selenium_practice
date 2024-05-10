import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(chrome_options)
driver.get(url="https://www.linkedin.com/jobs")

email_field = driver.find_element(By.XPATH, value="//div[@class='text-input flex']/input[@id='session_key']")
pass_field = driver.find_element(By.XPATH, value="//div[@class='text-input flex']/input[@id='session_password']")

email_field.send_keys("dogsmail@dog.me")
pass_field.send_keys("immapass", Keys.ENTER)
driver.get(url="https://www.linkedin.com/jobs/collections/recommended/")

time.sleep(2)
list_of_jobs = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
print(len(list_of_jobs))

for job in list_of_jobs:
    try:
        job.click()
        time.sleep(1)
        save = driver.find_element(By.CSS_SELECTOR,
                                   value="button[class='jobs-save-button artdeco-button artdeco-button--3 artdeco-button--secondary']")
        save.click()
        time.sleep(1)
    except:
        print("something wrong, check")
