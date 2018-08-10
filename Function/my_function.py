from Class.stock_daily_info import DailyInfoClass
from Module.stock_daily_info import get_db_last_date, get_stock_number_list
from datetime import datetime, date

# 將 json 物件轉成 DailyInfoClass
def mapping_daily_info(stock_number, daily_info, lastDateString):
	result = []

	for info in daily_info:
		trandingDate = convert_date(info[0])

		if is_late_date(lastDateString, trandingDate) == False:
			print(f"Date: {trandingDate} Is Exist!!")
			continue

		temp = DailyInfoClass()
		temp.stock_number = stock_number
		temp.tranding_date = convert_date(info[0])
		temp.trading_volume = int(info[1].replace(',',''))
		temp.trading_value = int(info[2].replace(',',''))
		temp.open = info[3]
		temp.high = info[4]
		temp.low = info[5]
		temp.close = info[6]
		temp.diff = info[7].replace('X','')
		temp.number_of_transations = int(info[8].replace(',',''))

		result.append(temp)

		print(f"Date: {trandingDate} Transfer Success")
	return result

# 將民國年轉成西元年
def convert_date(date_string):
	words = date_string.split('/')
	year = str(int(words[0]) + 1911)
	month = words[1]
	day = words[2]

	return f'{year}-{month}-{day}'

# 取得最後日期 yyyymmmdd
def get_last_date(stock_number):
	lastDate = get_db_last_date(stock_number)[0].strftime('%Y%m%d')

	return lastDate

# 是否大於最後日
def is_late_date(lastDateString, newDateString):
	lastDate = datetime.strptime(lastDateString, '%Y%m%d')
	newDate = datetime.strptime(newDateString, '%Y-%m-%d')

	return newDate > lastDate

# 取得 stock list
def get_stock_list():

	dbInfo = get_stock_number_list()

	stockNumberList = []

	for info in dbInfo:
		stockNumberList.append(info[0])

	return stockNumberList