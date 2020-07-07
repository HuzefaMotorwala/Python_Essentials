def isYearLeap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
    
def daysInMonth(year, month):
    monthdays=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    if isYearLeap(year)==True and month==2:
        monthdays[2]=29
    return monthdays[month]
print(daysInMonth(2012,2))    
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
