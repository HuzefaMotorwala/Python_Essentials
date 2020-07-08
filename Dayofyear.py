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
    
def dayOfYear(year, month, day):
    if year<1582:
        if month>12 or month<1:
            if day>31 or day<1:
                return None
    
    totdays = day
    month = month-1
    while month>0:
        totdays+=daysInMonth(year,month)
        month-=1
    return totdays    
    

print(dayOfYear(2000, 12, 31))
