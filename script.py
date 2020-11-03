from selenium import webdriver
import creds
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


username = creds.username
password = creds.password
driver = webdriver.Chrome(creds.driver)
repo = creds.repo
wait = WebDriverWait(driver, 5)


def login():
    # driver.maximize_window()
    #driver.get(repo)
    driver.get('https://github.com/login')
    username_box = wait.until(EC.element_to_be_clickable((By.NAME, 'login')))
    username_box.send_keys(username)
    pass_box = driver.find_element_by_name('password')
    pass_box.send_keys(password)
    submit_button = driver.find_element_by_name('commit')
    submit_button.click()
    driver.get(repo)

def make_change():
    writer = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="new_blob"]/div/div[5]/div[2]/div/div[5]/div[1]/div/div/div/div[5]/div/pre/span/span')))
    writer.send_keys('Hi!')


def commit():
    commit_button=driver.find_element_by_xpath('//*[@id="submit-file"]')
    commit_button.click()
    time.sleep(1)
    driver.close()

login()
make_change()
commit()
