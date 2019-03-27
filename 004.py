'''year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))
leap = 0
sum = 0
months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
if 0 < month <= 12:
    sum = months[month - 1]
    sum += day
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        leap = 1
    if (leap == 1) and (month > 2):
        sum += 1
    print('it is the %dth day' % sum)
else:
    print("data error")
    print('dataerror')
'''
def isLeapYear(year):
    return(year%400 == 0 and (year%4 == 0 and year%100 != 0))
DotM = [0,31,28,31,30,31,30,31,31,30,31,30]
sum = 0
year = int(input('year:'))
month = int(input('month'))
day = int(input('day'))
if 0<month<=12:
    if isLeapYear(year):
        DotM[2] += 1
    for i in range(month):
        sum += DotM[i]
    print(sum + day)
else:
    print ("data erro")
