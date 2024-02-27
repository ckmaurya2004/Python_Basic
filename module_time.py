import time

t = time.time()
print(t)
local_time = time.ctime(t)
print(local_time)#Wed Dec 27 09:17:04 2023

mytime=time.localtime(t)
print(mytime)#time.struct_time(tm_year=2023, tm_mon=12, tm_mday=27, tm_hour=9, tm_min=14, tm_sec=56, tm_wday=2, tm_yday=361, tm_isdst=0)
print(mytime.tm_year)
print(mytime.tm_wday )

 # localtime and gmtime is same

t1  = time.time()
current_time= time.gmtime(t1)
print(current_time)#time.struct_time(tm_year=2023, tm_mon=12, tm_mdatime.struct_time(tm_year=2023, tm_mon=12, tm_mday=27, tm_hour=3, tm_min=47, tm_sec=4, tm_wday=2, tm_yday=361, tm_isdst=0)y=27, tm_hour=3, tm_min=47, tm_sec=4, tm_wday=2, tm_yday=361, tm_isdst=0)
print(current_time.tm_year)
print(current_time.tm_hour)

# mktime is opposite of localtime  mktime take argument of tuple


mk_time=(2023,12,27,10,13,3,2,361,0)
local_time = time.mktime(mk_time)
print(local_time)#1703652183.0

mk_time=(2023,12,27,10,13,3,2,361,0)
local_time = time.asctime(mk_time)
print(local_time)#Wed Dec 27 10:13:03 2023