from Class.stock_daily_info import DailyInfoClass
from Module.db_base import Db_base

# 呼叫 insert stored procedure
def insert(info_list):
	for info in info_list:

		print(f'Process {info.stock_number}. Date => {info.tranding_date}')

		query = f"call insert_stock_daily_info('{info.stock_number}','{info.tranding_date}', {info.trading_volume}, {info.trading_value}, {info.open}, {info.high}, {info.low}, {info.close}, {info.diff}, {info.number_of_transations},'{info.create_date}', '{info.updated_date}')"
		
		print(query)

		db_base = Db_base()

		try:
			result = db_base.excute(query)

			if(result[0] != -1):
				print(f'Insert Success. Id => {result[0]}')
			else:
				print('Insert failure.')
		except:
			print(f'Excute Query Error!! {query}')

	db_base.dispose()

# insert 多筆
def insertList(info_list):
	query = "call insert_stock_daily_info(%(stock_number)s, %(tranding_date)s, %(trading_volume)s, %(trading_value)s, %(open)s, %(high)s, %(low)s, %(close)s, %(diff)s, %(number_of_transations)s, %(create_date)s, %(updated_date)s);"

	params = []

	for info in info_list:
		param = info.__dict__
		params.append(param)

	db_base = Db_base()
	db_base.executemany(query, params)

	db_base.dispose()
	


# 呼叫 get_predict_info
def get_predict_info(stock_number):
	query = f"call get_predict_info('{stock_number}')"

	db_base = Db_base()

	try:
		result = db_base.executeFetchAll(query)
	except:
		print('Db Error!!')

	db_base.dispose()

	return result

# 取得 db最後的日期
def get_db_last_date(stock_number):
	query = f"select tranding_date from stock_daily_info where stock_number = {stock_number} order by tranding_date desc limit 1;"

	db_base = Db_base()

	result = db_base.execute(query)

	return result
