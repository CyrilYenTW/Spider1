
import requests
import json
from Class.warrant_info import WarrantInfoClass
from operator import attrgetter
from Class.warrant_value_info import WarrantValueInfoClass

# 取得權證清單
def GetWarrantListDesc(stockNumber):
	url = f"http://warrant.cathaysec.com.tw/ws/WarSearch.aspx?showType=basic_123&p=CPCode,Derivative,Broker,Conver,Lever,,,Sp,Ep,S_Period,E_Period,BuySellRate,PageSize,PageNo,priority,listCode,Amt,Vol&v=1,ALL,ALL,ALL,ALL,,,-10000,10000,90,180,ALL,15000,1,888,{stockNumber},ALL,ALL"

	param = {
				"sEcho": "5",
				"iColumns": "17",
				"sColumns": "",
				"iDisplayStart": "0",
				"iDisplayLength": "20",
				"mDataProp_0": "0",
				"mDataProp_1": "1",
				"mDataProp_2": "2",
				"mDataProp_3": "3",
				"mDataProp_4": "4",
				"mDataProp_5": "5",
				"mDataProp_6": "6",
				"mDataProp_7": "7",
				"mDataProp_8": "8",
				"mDataProp_9": "9",
				"mDataProp_10": "10",
				"mDataProp_11": "11",
				"mDataProp_12": "12",
				"mDataProp_13": "13",
				"mDataProp_14": "14",
				"mDataProp_15": "15",
				"mDataProp_16": "16",
				"iSortCol_0": "13",
				"sSortDir_0": "desc",
				"iSortingCols": "1",
				"bSortable_0": "true",
				"bSortable_1": "true",
				"bSortable_2": "true",
				"bSortable_3": "true",
				"bSortable_4": "true",
				"bSortable_5": "true",
				"bSortable_6": "true",
				"bSortable_7": "true",
				"bSortable_8": "true",
				"bSortable_9": "true",
				"bSortable_10": "true",
				"bSortable_11": "true",
				"bSortable_12": "true",
				"bSortable_13": "true",
				"bSortable_14": "true",
				"bSortable_15": "true",
				"bSortable_16": "true"
			}

	jsonString = requests.post(url=url, data=param).text


	try:
		dataInfo = json.loads(jsonString)
		return dataInfo['aaData']
	except:
		return []

# 取得權證明細
def GetWarrantDetail(warrantCode):

	url = "http://warrant.cathaysec.com.tw/mFAT/GetInfo.aspx"

	params = {
		"f": "j",
		"u": "WARAllBI",
		"d": "DB_WARRANT",
		"t": "s",
		"c": "1",
		"p1": warrantCode,
		"521": ""
	}

	jsonString = requests.get(url=url, data=params).text
	
	result = json.loads(jsonString)

	return result

# 取得權證代號清單
def GetWarrantCodeList(stockNumber):
	codeList = []
	datas = GetWarrantListDesc(stockNumber)
	for data in datas:
		codeList.append(data[2])
	return codeList

# 取得權證資訊
def GetWarrantInfo(codeList):
	warrnatList = []

	for code in codeList:
		responseInfo = GetWarrantDetail(code)

		warrantInfo = responseInfo['items'][0]

		warrant = WarrantInfoClass()

		warrant.get_datetime = responseInfo['GT']
		warrant.stock_number = warrantInfo['X_UND_ID7']
		warrant.stock_price = warrantInfo['X_OBJ_TXN_PRICE']
		warrant.code = warrantInfo['X_ID7']
		warrant.strike_price = float(warrantInfo['X_N_STRIKE_PRC'])
		warrant.value_rate = float(warrantInfo['X_N_UND_CONVER'])
		warrant.outside_amount = int(warrantInfo['X_OUT_TOT_BAL_VOL'])
		warrant.rest_day = int(warrantInfo['X_TRANS_DAYS'])
		warrant.sell_price = float(warrantInfo['X_WAR_SELL_PRICE'])
		warrant.buy_price = float(warrantInfo['X_WAR_BUY_PRICE'])

		warrnatList.append(warrant)

	return warrnatList

# 主程序
def Main(stockNumber, stockGoal):

	codeList = GetWarrantCodeList(stockNumber)

	warrantList = GetWarrantInfo(codeList)

	warrantValueList = WarrantValueInfoClass()

	warrantValueInfoList = []

	for warrant in warrantList:
		temp = WarrantValueInfoClass()

		temp.stock_number = stockNumber
		temp.code = warrant.code
		temp.sell_price = float(warrant.sell_price)
		temp.value_rate = float(warrant.value_rate)
		temp.strike_price = float(warrant.strike_price)
		temp.stock_price = float(warrant.stock_price)
		temp.stock_goal = float(stockGoal)
		temp.warrant_value = float((temp.stock_price - temp.strike_price) * 1000 * temp.value_rate)
		temp.warrant_value_diff = float(temp.warrant_value - temp.sell_price * 1000)
		temp.warrant_goal_value = float((temp.stock_goal - temp.strike_price) * 1000 * temp.value_rate)
		temp.warrant_goal_value_diff = float(temp.warrant_goal_value - temp.sell_price * 1000)
		temp.rest_day = warrant.rest_day

		warrantValueInfoList.append(temp)

	warrantValueInfoList = sorted(warrantValueInfoList, key=attrgetter('warrant_value_diff'))

	print('股票代號\t權證編號\t權證價格\t履約價\t實行比例\t當前股價\t目標股價\t權證實際毛利\t權證目標價毛利\t剩餘天數')

	for data in warrantValueInfoList:
		temp = 	"%s\t%s\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.4f\t%.4f\t%s" % (data.stock_number, data.code, data.sell_price, data.strike_price, data.value_rate, data.stock_price, data.stock_goal, data.warrant_value_diff, data.warrant_goal_value_diff, data.rest_day)

		print(temp)

stockNumber = input("請輸入股票代碼:")
stockGoal = input("請輸入目標價格:")

Main(stockNumber, stockGoal)