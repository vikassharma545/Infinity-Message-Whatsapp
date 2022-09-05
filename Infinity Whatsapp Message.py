import os
import sys
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW('Infinite Whatsapp Message')
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

opts = Options()
opts.add_experimental_option("detach", True)
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=opts)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://web.whatsapp.com/")
os.system('cls')
input('\nLogin your Whatsapp after Successfull login press enter :) ')

chat_name = input('Entre Chat Name (should be in your contact list) : ')
driver.find_element(By.XPATH, """//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]""").send_keys(chat_name + Keys.ENTER)

if input('Open Correct chat window ? y/n :').lower() != 'y':
    sys.exit()
    
msg = input('Entre Message want to send : ')
sleep_time = int(input('Time between consecutive message in secounds : '))

while True:
    sleep(sleep_time)
    driver.find_element(By.XPATH, """//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]""").send_keys(chat_name + Keys.ENTER)
    driver.find_element(By.XPATH, """//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p""").send_keys(msg + Keys.ENTER)
