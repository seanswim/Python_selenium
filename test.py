import timer
import web_traveler
import asyncio
import time


web_traveler.open_website()
web_traveler.sign_in()
web_traveler.go_reservation(timer.current_date, timer.target_date_week, target_day_week)


