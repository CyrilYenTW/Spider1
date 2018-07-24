class WarrantInfoClass():

	def __init__(self):
		# 股票代號
		self.stock_number = ''

		# 股票現價
		self.stock_price = 0

		# 權證代碼
		self.code = ''

		# 權證型態
		self.type = 'buy'

		# 履約價
		self.strike_price = 0

		# 行使比例
		self.value_rate = 0

		# 在外流通量
		self.outside_amount = 0

		# 剩餘天數
		self.rest_day = 0

		# 賣價
		self.sell_price = 0

		# 買價
		self.buy_price = 0

		self.get_datetime = ''
