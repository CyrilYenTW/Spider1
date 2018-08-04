from Module import stock_daily_info

def Main(stock_number, day_range):
	day_range = int(day_range)

	infoList = stock_daily_info.get_predict_info(stock_number)

	rawInfo = []
	lastDate = ''

	for info in infoList:
		rawInfo.append(f'{info[1]}{info[2]}')
		lastDate = info[0]

	moduleList = {}
	lastModule = ''

	for i in range(0, len(infoList)):
		rawInfoList = rawInfo[i:i+day_range]

		key = ''

		for info in rawInfoList:
			key = f'{key}{info}'

		if i + day_range >= len(infoList):
			lastModule = key
			break

		nextStatus = rawInfo[i+day_range][1]

		if moduleList.get(key) == None:
			moduleList[key] = {'0':0, '1':0, '2':0}
			moduleList[key][nextStatus] += 1
		else:
			moduleList[key][nextStatus] += 1

	# 不存在 Module
	if moduleList.get(lastModule) == None:
		print(f'Last Date = {lastDate}')
		print(f'Last Module = {lastModule}')
		print('This Module Not Exist')
		return

	totalCount = moduleList[lastModule]['0'] + moduleList[lastModule]['1'] + moduleList[lastModule]['2']

	up = moduleList[lastModule]['2']
	down = moduleList[lastModule]['0']
	normal = moduleList[lastModule]['1']

	result = "Total Count = %s','Up Count = %s, %.2f％','Noraml Count = %s, %.2f％','Down Count = %s, %.2f％" % (totalCount, up, up/totalCount*100, normal, normal/totalCount*100, down, down/totalCount*100)

	print(f'Last Date = {lastDate}')
	print(f'Last Module = {lastModule}')
	print(result)

stockNumber = input("stock number => ")
dayRange = input("day range => ")

Main(stockNumber, dayRange)

