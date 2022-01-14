from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager



def open_website():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = 'https://www.yangsancc.co.kr/'
    return driver.get(url)


open_website()
