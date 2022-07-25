import datetime
str = '20211112T213839,011118' # 剪辑到秒的小数点后两位
date = str.split('T')[0]
time = str.split('T')[1]
time_high = time.split(',')[0]
time_low = time.split(',')[1]

format_year = date[:4]
print(format_year)
format_mon = date[4:6]
print(format_mon)
format_days = date[6:8]
print(format_days)
format_hh = time_high[:2]
print(format_hh)
format_mm = time_high[2:4]
print(format_mm)
format_ss = time_high[4:6] + '.' + time_low[:2]
print(format_ss)

# datetime_object = datetime.datetime.now()
# print(datetime.datetime(2017, 10, 7, 0, 1,12))
