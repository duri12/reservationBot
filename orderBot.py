from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import subprocess

PATH_TO_CHROMEDRIVER = r"C:\Program Files (x86)\chromedriver.exe"
PATH_TO_CHROME = r'C:\Users\eyal\AppData\Local\Google\Chrome\User Data'

# this program is my first attempt using selenium
# the plan is to make a program that automates tha reservation process
# TODO: make global variables for time / room
#       add docs , clean code , auto run , virtual adder


def setDriverOptions():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument(f"--user-data-dir={PATH_TO_CHROME}")
    options.add_argument(r'--profile-directory=Default')
    return options


def makeOrder(driver):
    start_select = Select(driver.find_element(By.ID,"BeginPeriod"))
    start_select.select_by_visible_text("17:00")
    ending_select = Select(driver.find_element(By.ID,"EndPeriod"))
    ending_select.select_by_visible_text("19:00")
    title = driver.find_element(By.ID,"reservationTitle")
    title.send_keys('shimi tavory <3')
    time.sleep(2)
    send = driver.find_element(By.XPATH, '//*[@id="form-reservation"]/div[6]/div/div/button[2]')
    send.click()


def navigateToOrder(driver):
    driver.get("https://bookme.technion.ac.il/booked/Web/schedule.php?sid=5")
    time.sleep(3)
    go2Weeks(driver)
    room = driver.find_element(By.XPATH, '//*[@id="reservations"]/table[1]/tbody/tr[24]/td[1]/a')
    room.click()


def go2Weeks(driver):
    for _ in [1, 2]:
        time.sleep(1)
        link = driver.find_element(By.XPATH,'//*[@id="page-schedule"]/div[2]/div[3]/a[3]')
        driver.execute_script("arguments[0].click();",link)


def main():
    subprocess.call("TASKKILL /f /IM CHROME.EXE")
    time.sleep(1)
    options = setDriverOptions()
    service = Service(PATH_TO_CHROMEDRIVER)
    driver = webdriver.Chrome(service=service, options=options)
    navigateToOrder(driver)
    makeOrder(driver)
    time.sleep(5)
    driver.quit()

if __name__ == '__main__':
    main()

