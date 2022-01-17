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


def go_reservation(current_date, raw_target_date, target_day_week):
    try:
        year = current_date.year
        month = current_date.month
        day = current_date.day
        point_date = str(year) + str(month) + str(day)

        # Declare target_date
        target_year = raw_target_date.year
        target_month = raw_target_date.month
        target_day = raw_target_date.day
        if len(str(month - 1)) == 1:
            target_date = str(target_year) + '0' + str(target_month) + str(target_day)
        else:
            target_date = str(target_year) + str(target_month) + str(target_day)

        # Declare now_date
        if len(str(month - 1)) == 1:
            now_date = str(year) + '0' + str(month)
        else:
            now_date = str(year) + str(month)

        # Declare prev_date
        if month - 1 == 0:
            prev_date = str(year - 1) + '12'
        else:
            if len(str(month - 1)) == 1:
                prev_date = str(year) + '0' + str(month - 1)
            else:
                prev_date = str(year) + str(month - 1)

        # Declare next_date
        if month + 1 == 13:
            next_date = str(year + 1) + '01'
        else:
            if len(str(month - 1)) == 1:
                next_date = str(year) + '0' + str(month + 1)
            else:
                next_date = str(year) + str(month + 1)

        url = f'https://www.yangsancc.co.kr/pagesite/reservation/live.asp'
        driver.get(url)
        driver.implicitly_wait(20)
        second_url = f'javascript:timefrom_change({target_date},"1",{target_day_week},"","00","T"'
        # second_url = f'https://yangsancc.co.kr/GolfRes/onepage/real_reservation.asp?#pointdate={target_date}&courseid=3&openyn=1&dategbn=2&choice_time=00&settype=T&prevDate={prev_date}&nowDate={now_date}&nextDate={next_date}'
        print(second_url)
        driver.get(second_url)
    except:
        print('go_reservation error!')

