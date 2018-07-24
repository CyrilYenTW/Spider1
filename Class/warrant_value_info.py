class WarrantValueInfoClass():

	def __init__(self):
		# 標的股票代號
		self.stock_number = 0

		self.code = ''

		# 權證價格
		self.sell_price = 0

		# 行使比例
		self.value_rate = 0.0

		# 履約價
		self.strike_price = 0

		# 當前股價
		self.stock_price = 0

		# 目標股價
		self.stock_goal = 0

		# 權證價值
		self.warrant_value = 0

		# 權證毛利
		self.warrant_value_diff = 0

		# 達標價值
		self.warrant_goal_value = 0

		# 達標毛利
		self.warrant_goal_value_diff =0