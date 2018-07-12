import pymysql

# 資料庫連線模組
class Db_base():

	def __init__(self):
		self.db = pymysql.connect(
				"domain",
				"account",
				"password",
				"dbname")

	# dispose
	def dispose(self):
		self.db.close()

    # excute
	def excute(self, query):
		cursor = self.db.cursor()
		cursor.execute(query)
		result = cursor.fetchone()
		return result

