import requests
import json
from my_function import mapping_daily_info
from Module.stock_daily_info import DailyInfoClass

stock_number = '2345'
date_sting = '20180601'
url = f'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={date_sting}&stockNo={stock_number}&_=1531358889990'

daily_info_string = requests.get(url)
daily_info = json.loads(daily_info_string.text)

info_list = []

if(daily_info['stat'] == 'OK' and len(daily_info['data']) > 0):
	info_list = mapping_daily_info(stock_number, daily_info['data'])
