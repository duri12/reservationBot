from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


PATH_TO_CHROMEDRIVER = r"C:\Program Files (x86)\chromedriver.exe"



def set_driver_options():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument(r'--profile-directory=Default')
    return options


def print_start_options():
    """
    this function prints the starting messages
    """
    print("--------------------------------------------------")
    print("| welcome to the group spammer                   |")
    print("| to spam without a message press 1              |")
    print("| to spam with a message press 2                 |")
    print("| to exit press 0                                |")
    print("|                                   ▄▄█▀▀▀▀▀█▄▄  |")
    print("|                                 ▄█▀░░▄▄░░░░░▀█▄|")
    print("|                                 █░░░███░░░░░░░█|")
    print("|                                 █░░░██▄░░░░░░░█|")
    print("|                                 █░░░░▀██▄░██░░█|")
    print("|                                 █░░░░░░▀███▀░░█|")
    print("|                                 ▀█▄░░░░░░░░░▄█▀|")
    print("|                                  ▄█░░░▄▄▄▄█▀▀  |")
    print("|                                  █░░▄█▀        |")
    print("|                                  ▀▀▀▀          |")
    print("--------------------------------------------------")


def get_starting_params():
    """
    this function gets the params from the user
    and starts the spam
    :return: a list with the starting params as follows :
    [ option (mandatory) ,target (mandatory),extra params]
    """
    msg = ""
    print_start_options()
    option = int(input())
    while option not in [0, 1, 2]:
        print("not a valid option please try again")
        option = int(input())
    if option == 2:
        print("please enter the message you would like to be spammed")
        msg = input()
    print("please enter the target's nickname or number")
    phoneNumber = input()
    return [option, phoneNumber , msg] if msg != "" else [option,phoneNumber]

def create_group(driver ,target , msg):
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[3]/header/div[2]/div/span/div[3]' ).click()

def main():
    startingParams = get_starting_params()
    options = set_driver_options()
    service = Service(PATH_TO_CHROMEDRIVER)
    driver = webdriver.Chrome(service=service, options=options)
    if startingParams[0] != 0:
        driver.get("https://web.whatsapp.com/")
        print("Scan QR Code, And then Enter")
        input()
        print("Logged In")
    input()
    driver.quit()


if __name__ == '__main__':
    main()
