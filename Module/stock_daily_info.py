import datetime

class DailyInfoClass():

	def __init__(self):
		self.stock_number = ''
		self.date = ''
		self.trading_volume = 0
		self.trading_value = 0
		self.open = 0
		self.high = 0
		self.low = 0
		self.close = 0
		self.diff = 0
		self.number_of_transations = 0
		self.create_date = datetime.datetime.now
		self.updated_date = datetime.datetime.now
