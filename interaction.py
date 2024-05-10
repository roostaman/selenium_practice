from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

article_element = driver.find_element(By.XPATH, value="//div[@id='articlecount']/a[@title='Special:Statistics']")

article_count = article_element.text
# print(article_count)
article_element.click()

search = driver.find_element(By.CLASS_NAME, value="cdx-text-input__input")
search.send_keys("turks", Keys.ENTER)

# driver.quit()
