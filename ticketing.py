from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from time import strftime
import time
import datetime
from datetime import timedelta
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = 'https://www.yangsancc.co.kr/'
date = datetime.datetime.now().weekday()
now = time.strftime("%H:%M:%S", time.localtime(time.time()))
a = 0
day = datetime.datetime.now()
reservationW = day + timedelta(days=14)
reservationE = day + timedelta(days=18)
reservationDateW = reservationW.strftime('%#d')
reservationDateE = reservationE.strftime('%#d')

#open website
driver.get(url)

#process1: signin
driver.find_element(by='id', value='log_id').send_keys('jun3411')
driver.find_element(by='id', value='login_pw').send_keys('kjw3254')
driver.find_element(by='id', value='login_pw').send_keys(Keys.ENTER)
Alert(driver).accept()
print('로그인이 완료되었습니다.')

#process2: Standby the thread until 9am if its Tuesday or Thursday
if date == 1 or date == 3 or date == 4:
    while now < '09:00:00':
        time.sleep(0.3)
        a += 0.5
        now = time.strftime("%H:%M:%S", time.localtime(time.time()))
        print('프로그램 대기중입니다 | {} 초 경과 | 현재시간 {}'.format(a, now))
    print('예약 프로세스를 시작합니다')
    driver.get('https://www.yangsancc.co.kr/pagesite/reservation/live.asp')
    driver.implicitly_wait(20)
    # process3: pick a date
    if day.month == reservationW.month:
        driver.find_elements_by_link_text(reservationDateW)[0].click()
    else:
        driver.find_elements_by_link_text(reservationDateW)[1].click()
    elCheck = driver.page_source
    soup = BeautifulSoup(elCheck, "lxml")
    a = soup.find('div', attrs={'class': 'cm_time_popup_content'})
    if a != None:
        while a != None:
            driver.refresh()
            time.sleep(0.2)
            driver.implicitly_wait(20)
            print('페이지를 새로고침합니다.')
    elif a == None:
        print('예약을 진행하십시오')
    else:
        print('예상치못한 페이지')
    # process4: pick a time
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    d = []
    e = []
    a = soup.find_all('td', attrs={'class': 'cm_qjsgh'})
    for i in a:
        i = i.get_text()
        d.append(i)
    b = soup.find_all('td', attrs={'class': 'cm_zhtm'})
    for i in b:
        i = i.get_text()
        e.append(i)
    indexC = 0
    count = 0
    for i in e:
        indexC += 1
        if i == '마루':
            count += 1
            if count == 3:
                break
            indexV = e.index(i)
    driver.find_elements_by_class_name('cm_dPdir')[indexC].click()
    print(d)
    print(e)
    print(indexC)
    driver.find_element_by_class_name('cm_dPdir').click()

elif date == 2:
    while now < '10:00:00':
        time.sleep(0.5)
        a += 0.5
        now = time.strftime("%H:%M:%S", time.localtime(time.time()))
        print('프로그램 대기중입니다 | {} 초 경과 | 현재시간 {}'.format(a, now))
    print('예약 프로세스를 시작합니다')
    driver.get('https://www.yangsancc.co.kr/pagesite/reservation/live.asp')
    driver.implicitly_wait(20)
    # process3: pick a date
    if day.month == reservationE.month:
        driver.find_elements_by_link_text(reservationDateE)[0].click()
    else:
        driver.find_elements_by_link_text(reservationDateE)[1].click()
    driver.implicitly_wait(20)
    # process4: pick a time
    html = driver.page_source
    print(html)

else:
    print('예약할 수 있는 요일이 아닙니다.')

