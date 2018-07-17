# -*- coding: utf-8 -*-

import requests
import json
import sys
from Class.stock_week_info import WeekInfoClass
from bs4 import BeautifulSoup as bs
from Module.stock_week_info import Insert

# 取得 header
def GetHeaders():
	headers = 	{		
					"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,gd;q=0.5",
					"Cache-Control": "max-age=0",
					"Connection": "keep-alive",
					"Content-Length": "121",
					"Content-Type": "application/x-www-form-urlencoded",
					"Host": "www.tdcc.com.tw",
					"Origin": "https://www.tdcc.com.tw",
					"Referer": "https://www.tdcc.com.tw/smWeb/QryStockAjax.do",
					"Upgrade-Insecure-Requests": "1",
					"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
				}
	return headers


# 取得日期區間
def GetDateRange():
	url = 'https://www.tdcc.com.tw/smWeb/QryStockAjax.do'

	param = {}
	param['REQ_OPR'] = 'qrySelScaDates'
	headers = GetHeaders()

	try:
		pageInfo = requests.post(url=url, headers=headers, data=param)
		result = json.loads(pageInfo.text)

		return result
	except:
		return []


# 取得每周集保戶股權分散
def GetStockWeekPageInfo(dateString, stockNumber):
	url = 'https://www.tdcc.com.tw/smWeb/QryStockAjax.do'
	param = {}

	param['scaDates'] = dateString
	param['scaDate'] = dateString
	param['SqlMethod'] = 'StockNo'
	param['StockNo'] = stockNumber
	param['radioStockNo'] = stockNumber
	param['StockName'] = ''
	param['REQ_OPR'] = 'SELECT'
	param['clkStockNo'] = stockNumber
	param['clkStockName'] = ''

	headers = GetHeaders()

	try:
		pageText = requests.post(url, headers=headers, data=param)
	except:
		return ''

	return pageText.text


# 取得 每周集保戶股權分散 物件清單
def GetStockWeekInfoList(weekDate, stockNumber):

	weekInfoString = ''

	# 防止Response 為空
	while weekInfoString == '':
		weekInfoString = GetStockWeekPageInfo( weekDate, stockNumber)

	soup = bs(weekInfoString, 'html.parser')

	# 找到 Table
	rows = soup.find_all(attrs={'class':'mt'})[1].find_all('tr')

	weekInfoList = []

	for row in rows[1:]:
		# 分解欄位
		columns = row.find_all('td')

		temp = WeekInfoClass()

		temp.week_date = weekDate
		temp.stock_number = stockNumber

		# 去掉合計那列
		if columns[1].string.find('合') != -1 or columns[1].string.find('差') != -1:
			continue

		rangeInfo = columns[1].string.replace('以上', '').replace(',', '').split('-')

		rangeStart = rangeInfo[0]
		rangeEnd = rangeInfo[1] if len(rangeInfo)>1 else '999999999'
		
		temp.range_start = rangeStart
		temp.range_end = rangeEnd
		temp.owner_count = columns[2].string.replace(',', '')
		temp.total_stock_amount = columns[3].string.replace(',', '')
		temp.own_rate = columns[4].string

		weekInfoList.append(temp)

	return weekInfoList



def main(stockNumber):
	dateRange = []

	# 取得 Data Range
	while dateRange == []:
		dateRange = GetDateRange()

	for weekDate in dateRange:
		weekInfoList = GetStockWeekInfoList(weekDate, stockNumber)
		Insert(weekInfoList)

main('2345')