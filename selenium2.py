from selenium import webdriver
import time 
import parameters
import getpass
import requests
from selenium.webdriver.common.keys import Keys


driver_path = "/home/nur/Desktop/Python/yeni/selenium/chromedriver"

driver = webdriver.Chrome(driver_path)

userid = str(input("Email adresi veya telefon numarasi giriniz : "))
password = getpass.getpass('Parola giriniz :')

driver.get("https://www.linkedin.com/uas/login?_l=tr")


driver.implicitly_wait(6)
driver.find_element_by_xpath("""//*[@id="username"]""").send_keys(userid)
driver.find_element_by_xpath("""//*[@id="password"]""").send_keys(password)
driver.find_element_by_xpath("""//*[@type="submit"]""").click()
time.sleep(2)
driver.maximize_window()
#driver.find_element_by_xpath("""//*[@id="ember161"]""").click()
driver.get("https://www.linkedin.com/mynetwork/")
time.sleep(4)


def baglanti_kur():
    buttons = driver.find_elements_by_xpath("""//button[@data-control-name='invite']""")
    for i in buttons:
        i.click()

baglanti_kur()       