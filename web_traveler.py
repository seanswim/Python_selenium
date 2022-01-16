from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from dotenv import load_dotenv
import os
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
load_dotenv(verbose=True)


def open_website():
    try:
        url = 'https://www.yangsancc.co.kr/'
        driver.get(url)
    except:
        print('open_website error!')


def sign_in():
    try:
        driver.find_element(by='id', value='log_id').send_keys(os.getenv('ID'))
        driver.find_element(by='id', value='login_pw').send_keys(os.getenv('PASSWORD'))
        driver.find_element(by='id', value='login_pw').send_keys(Keys.ENTER)
        Alert(driver).accept()
        print('로그인이 완료되었습니다.')
    except:
        print('sign_in error!')


def go_reservation(current_date):
    try:
        year = current_date("%Y")
        month = current_date("%m")
        date = current_date("%d")
        point_date = year + month + date
        now_date = year + month
        if int(month) - 1 == 0:
            prev_date = (int(year) - 1) + '12'
        else:
            if len(int(month) - 1) == 1:
                prev_date = year + '0' + (int(month) - 1)
            else:
                prev_date = year + (int(month) - 1)
        if int(month) + 1 == 13:
            next_date = (int(year) + 1) + '01'
        else:
            if len(int(month) - 1) == 1:
                next_date = year + '0' + (int(month) + 1)
            else:
                next_date = year + (int(month) + 1)
        url = f'https://yangsancc.co.kr/GolfRes/onepage/real_reservation.asp?#pointdate={point_date}&courseid=3&openyn=1&dategbn=2&choice_time=00&settype=T&prevDate={prev_date}&nowDate={now_date}&nextDate={next_date}'
        driver.get(url)
    except:
        print('go_reservation error!')
