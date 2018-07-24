# -*- coding: UTF-8 -*-

import requests
import json
from datetime import datetime, date
from Function.my_function import mapping_daily_info
from Class.stock_daily_info import DailyInfoClass
from Module.stock_daily_info import insert

# 取得交易資料
def get_info(stock_number, date_sting):
	# 交易所網址
	url = f'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={date_sting}&stockNo={stock_number}&_=1531358889990'

	daily_info_string = requests.get(url)
	daily_info = json.loads(daily_info_string.text)

	info_list = []

	if(daily_info['stat'] == 'OK' and len(daily_info['data']) > 0):
		# 將json物件轉成自訂物件
		info_list = mapping_daily_info(stock_number, daily_info['data'])

		# 新增數據
		insert(info_list)


# 取得下一個月的日期
def get_next_month(date_string):
	year = date_string[0:4]

	month = date_string[4:6]
	
	if (int(month)+1 > 12):
		year = str(int(year) + 1)
		month = '01'
	else:
		month = str(int(month) + 1)
	

	return datetime.strptime(year+month, '%Y%m')

# 主程式
def main():
	stock_number = input("請輸入股票代號 => ")
	start_date_string = input("請輸入起始年月(yyyymm) =>")

	start_date = datetime.strptime(start_date_string, '%Y%m')

	while datetime.now() > start_date:
		start_date_string = datetime.strftime(start_date, '%Y%m') + '01'

		print(f'Process Moth => {start_date_string}')

		start_date = get_next_month(start_date_string)
		get_info(stock_number, start_date_string)

main()