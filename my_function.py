from Module.stock_daily_info import DailyInfoClass

def mapping_daily_info(stock_number, daily_info):
	result = []

	for info in daily_info:
		temp = DailyInfoClass()
		temp.stock_number = stock_number
		temp.date = info[0]
		temp.trading_volume = info[1]
		temp.trading_value = info[2]
		temp.open = info[3]
		temp.high = info[4]
		temp.low = info[5]
		temp.close = info[6]
		temp.diff = info[7]
		temp.number_of_transations = info[8]

		result.append(temp)

	return result