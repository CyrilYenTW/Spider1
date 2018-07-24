import datetime

class WeekInfoClass():

	def __init__(self):
		# 統計時間
		self.week_date = ''

		# 股票代碼
		self.stock_number = ''

		# 範圍起
		self.range_start = 0

		# 範圍迄
		self.range_end = 0

		# 持有人數量
		self.owner_count = 0

		# 總持股數
		self.total_stock_amount = 0

		# 持股比例
		self.own_rate = 0.0

		# 新增日期
		self.create_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

		# 更新日期
		self.updated_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')