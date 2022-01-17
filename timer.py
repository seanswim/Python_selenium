import time
import datetime
from datetime import timedelta

#현재시간
current_time = time.strftime("%H:%M:%S", time.localtime(time.time()))
#오늘날짜
current_date = datetime.datetime.now()
#오늘요일
current_day = datetime.datetime.now().weekday()
#평일예약일
target_date_week = current_date + timedelta(days=14)
#예약일요일
target_day_week = target_date_week.weekday()

#주말예약일
if current_day == 3:
    target_date_weekend = current_date + timedelta(days=18)
else:
    target_date_weekend = -1


def is_valid_time():
    now = time.strftime("%H:%M:%S", time.localtime(time.time()))
    if now >= '09:00:00':
        return true
    else:
        return false


print(target_day_week)