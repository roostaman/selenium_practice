from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.python.org/")

upcoming_events = {}

events_element = driver.find_elements(By.XPATH, value="//div[@class='medium-widget event-widget last']/div/ul/li")

try:
    i = 0
    for element in events_element:
        date_element = element.find_element(By.XPATH, value=".//time")
        event_element = element.find_element(By.XPATH, value=".//a")
        upcoming_events[i] = {'time': date_element.text, 'name': event_element.text}
        i += 1

except Exception as ex:
    print(ex)

print(upcoming_events)

driver.quit()
