import datetime 

print(dir(datetime))

# Date class 
print(datetime.date.today()) # the current date

d = datetime.date(2019, 4, 13)
print(type(d))
print(d)

print(d.day)
print(d.month)
print(d.year)

print(type(d.strftime("%d---->%m------>%Y")))
print(d.strftime("%d---->%m------>%Y"))

# Datetime class 
print(datetime.datetime.now())

dt = datetime.datetime(2022, 11, 12, 15,40,10,000000)

print(type(dt))
print(dt)

print(dt.day)
print(dt.month)
print(dt.year)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)

print(type(dt.strftime("%d---->%m------>%Y ::::::%H::::::%M::::::%S::::::%f")))
print(dt.strftime("%d---->%m------>%Y ::::::%H::::::%M::::::%S::::::%f"))

# time module not within the datetime module
#For Unix system, January 1, 1970, 00:00:00 at UTC is epoch (the point where time begins).
import time 
seconds = time.time()
print(seconds)
# seconds passed since epoch
local_time = time.ctime(seconds+3600)
print("Local time:", local_time)

time.sleep(2.4)
print("This is printed after 2.4 seconds.")


# how to convert a string to a datetime 
str_date = "2022/11/12 15:41:20"
datetime_obj = datetime.datetime.strptime(str_date,"%Y/%m/%d %H:%M:%S")
print(type(datetime_obj))
print(datetime_obj)


my_diff = datetime_obj - dt

print(type(my_diff))
print(my_diff)

print(my_diff.days)
print(my_diff.seconds)
print(my_diff.total_seconds()/60)

print(my_diff.min)
print(my_diff.max)

import math
print(dir(math))
