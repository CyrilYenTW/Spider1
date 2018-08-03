from Class.stock_daily_info import DailyInfoClass

# 將 json 物件轉成 DailyInfoClass
def mapping_daily_info(stock_number, daily_info):
	result = []

	for info in daily_info:
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

	return result

# 將民國年轉成西元年
def convert_date(date_string):
	words = date_string.split('/')
	year = str(int(words[0]) + 1911)
	month = words[1]
	day = words[2]

	return f'{year}-{month}-{day}'