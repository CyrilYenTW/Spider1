from Class.stock_daily_info import DailyInfoClass
from Module.db_base import Db_base

# 呼叫 insert stored procedure
def insert(info_list):
	for info in info_list:

		print(f'Process {info.stock_number}. Date => {info.date}')

		query = f"call insert_stock_daily_info('{info.stock_number}','{info.date}', {info.trading_volume}, {info.trading_value}, {info.open}, {info.high}, {info.low}, {info.close}, {info.diff}, {info.number_of_transations},'{info.create_date}', '{info.updated_date}')"
		db_base = Db_base()
		result = db_base.excute(query)
		
		if(result[0] != -1):
			print(f'Insert Success. Id => {result[0]}')
		else:
			print('Insert failure.')

	db_base.dispose()