from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from dotenv import load_dotenv
import os
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
load_dotenv(verbose=True)


def open_website():
    url = 'https://www.yangsancc.co.kr/'
    driver.get(url)


def sign_in():
    driver.find_element(by='id', value='log_id').send_keys(os.getenv('ID'))
    driver.find_element(by='id', value='login_pw').send_keys(os.getenv('PASSWORD'))
    driver.find_element(by='id', value='login_pw').send_keys(Keys.ENTER)
    Alert(driver).accept()
    print('로그인이 완료되었습니다.')


