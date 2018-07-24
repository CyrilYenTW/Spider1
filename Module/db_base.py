import pymysql

# 資料庫連線模組
class Db_base():

	def __init__(self):
		self.db = pymysql.connect(
				"xxx",
				"xxx",
				"xxx",
				"spider1")

	# dispose
	def dispose(self):
		self.db.close()

    # excute
	def excute(self, query):
		cursor = self.db.cursor()
		cursor.execute(query)
		result = cursor.fetchone()
		return result

	# excutemay
	def executemany(self, query, params):
		cursor = self.db.cursor()
		cursor.executemany(query, params)
