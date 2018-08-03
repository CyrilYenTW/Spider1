from Module import stock_daily_info

def Main(stock_number):
	infoList = stock_daily_info.get_predict_info(stock_number)

	rawInfo = []
	lastDate = ''

	for info in infoList:
		rawInfo.append(f'{info[1]}{info[2]}')
		lastDate = info[0]

	moduleList = {}
	lastModule = ''

	for i in range(0, len(infoList)):
		key = f'{rawInfo[i]}{rawInfo[i+1]}{rawInfo[i+2]}'

		if i+3 >= len(infoList):
			lastModule = key
			break

		nextStatus = rawInfo[i+3][1]

		if moduleList.get(key) == None:
			moduleList[key] = {'0':0, '1':0, '2':0}
			moduleList[key][nextStatus] += 1
		else:
			
			moduleList[key][nextStatus] += 1

	totalCount = moduleList[lastModule]['0'] + moduleList[lastModule]['1'] + moduleList[lastModule]['2']

	up = moduleList[lastModule]['2']
	down = moduleList[lastModule]['0']
	normal = moduleList[lastModule]['1']

	result = "Total Count = %s\nUp Count = %s, %.2f％\nNoraml Count = %s, %.2f％\nDown Count = %s, %.2f％" % (totalCount, up, up/totalCount*100, normal, normal/totalCount*100, down, down/totalCount*100)

	print(f'Last Date = {lastDate}')
	print(f'Last Module = {lastModule}')
	print(result)

stockNumber = input("stock number => ")
Main(stockNumber)

