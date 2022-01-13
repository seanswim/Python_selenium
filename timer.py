import time
import datetime
from datetime import timedelta

#현재시간
current_time = time.strftime("%H:%M:%S", time.localtime(time.time()))
#오늘날짜
current_date = datetime.datetime.now()
#오늘요일
current_day = date = datetime.datetime.now().weekday()
#평일예약일
target_date_week = current_date + timedelta(days=14)
#주말예약일
if current_day == 3:
    target_date_weekend = current_date + timedelta(days=18)
else:
    target_date_weekend = -1



