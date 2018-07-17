from Class.stock_week_info import WeekInfoClass
from Module.db_base import Db_base

def Insert(weekInfoList):
	
	stock_number = weekInfoList[0].stock_number
	week_date = weekInfoList[0].week_date

	print(f'Process {stock_number} {week_date}')

	query = "call insert_stock_week_info(%(week_date)s, %(stock_number)s, %(range_start)s, %(range_end)s, %(owner_count)s, %(total_stock_amount)s, %(own_rate)s, %(create_date)s, %(updated_date)s);"
	params = []

	for weekInfo in weekInfoList:
		param = weekInfo.__dict__
		params.append(param)

	db_base = Db_base()
	db_base.executemany(query, params)



