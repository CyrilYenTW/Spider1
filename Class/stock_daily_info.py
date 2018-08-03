import datetime

class DailyInfoClass():

	def __init__(self):
		# 股票代號
		self.stock_number = ''

		# 交易日
		self.tranding_date = ''

		#總成交股數
		self.trading_volume = 0

		# 總成交金額
		self.trading_value = 0

		# 開盤價
		self.open = 0

		# 最高價
		self.high = 0

		# 最低價
		self.low = 0

		# 收盤價
		self.close = 0

		# 價差
		self.diff = 0

		# 成交單量
		self.number_of_transations = 0

		# 新增日期
		self.create_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

		# 更新日期
		self.updated_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
