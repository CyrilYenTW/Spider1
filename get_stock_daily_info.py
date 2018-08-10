# -*- coding: UTF-8 -*-

import requests
import json
import time
from datetime import datetime, date
from Function.my_function import mapping_daily_info, get_last_date, get_stock_list
from Class.stock_daily_info import DailyInfoClass
from Module.stock_daily_info import insert, insertList

# 取得交易資料
def get_info(stock_number, date_sting, lastDateString = '19900101'):
	# 交易所網址
	url = f'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={date_sting}&stockNo={stock_number}&_=1531358889990'

	daily_info_string = requests.get(url)
	daily_info = json.loads(daily_info_string.text)

	info_list = []

	if(daily_info['stat'] == 'OK' and len(daily_info['data']) > 0):
		# 將json物件轉成自訂物件
		info_list = mapping_daily_info(stock_number, daily_info['data'], lastDateString)

		# 新增數據
		#insert(info_list)
		insertList(info_list)


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
def new_daily_info():
	stock_number = input("請輸入股票代號 => ")

	start_date_string = input("請輸入起始年月(yyyymm) =>")

	start_date = datetime.strptime(start_date_string, '%Y%m')

	while datetime.now() > start_date:
		start_date_string = datetime.strftime(start_date, '%Y%m') + '01'

		print(f'Process Moth => {start_date_string}')

		start_date = get_next_month(start_date_string)
		get_info(stock_number, start_date_string)

		time.sleep(2)

# 更新資料庫
def update_daily_info():
	stockNumberList = get_stock_list();

	for stockNumber in stockNumberList:

		print(f"\nProcess {stockNumber}")

		lastDateString = get_last_date(stockNumber)

		lastMonthString = lastDateString[0:6]

		startDate = datetime.strptime(lastMonthString, '%Y%m')

		while datetime.now() > startDate:
			startDateString = datetime.strftime(startDate, '%Y%m') + '01'

			print(f'Process Moth => {startDateString}')

			startDate = get_next_month(startDateString)

			get_info(stockNumber, startDateString, lastDateString)

			time.sleep(2)

	print('Process Update Done!!')


def Main():
	selection = input("請選擇[1.新增股票, 2.更新] : ")

	if selection == '1':
		new_daily_info()
	elif selection == '2':
		update_daily_info()

Main()