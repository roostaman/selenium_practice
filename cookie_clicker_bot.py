from selenium import webdriver
from selenium.webdriver.common.by import By
import time

CURSOR = 15
GRANDMA = 100
FACTORY = 500
MINE = 2000
SHIPMENT = 7000
ALCHEMY = 50000
PORTAL = 1000000
MACHINE = 123456789
rank = 1


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome()
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.XPATH, value="//div[@id='cookie'][@onmouseup]")


def check_money():
    global rank
    money_element = (driver.find_element(By.XPATH, value="//div[@id='money']")).text

    if "," in money_element:
        money_element = money_element.replace(",", "")
    money = int(money_element)

    if money >= CURSOR and rank == 1:
        buy = driver.find_element(By.ID, value="buyCursor")
        buy.click()
        rank += 1
    elif money >= GRANDMA and rank == 2:
        buy = driver.find_element(By.ID, value="buyGrandma")
        buy.click()
        rank += 1
    elif money >= FACTORY and rank == 3:
        buy = driver.find_element(By.ID, value="buyFactory")
        buy.click()
        rank += 1
    elif money >= MINE and rank == 4:
        buy = driver.find_element(By.ID, value="buyMine")
        buy.click()
        rank += 1


start_time = time.time()
five_mins = start_time + 20

while True:
    cookie.click()
    check_time = start_time - time.time()
    if check_time >= 5:
        check_money()
    if time.time() > five_mins:
        result = (driver.find_element(By.ID, value="cps")).text
        print(result)

        break
