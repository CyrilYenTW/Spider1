# -*- coding: UTF-8 -*-

import requests

url = 'https://www.tdcc.com.tw/smWeb/QryStockAjax.do'

param = {}

param['scaDates'] = '20170407'
param['scaDate'] = '20170407'
param['SqlMethod'] = 'StockNo'
param['StockNo'] = 2345
param['radioStockNo'] = 2345
param['StockName'] = ''
param['REQ_OPR'] = 'SELECT'
param['clkStockNo'] = 2345
param['clkStockName'] = ''

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

temp = requests.post(url, headers=headers, data=param)

print(temp.text)


