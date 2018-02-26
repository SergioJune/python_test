#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习内建模块致datetime'

__author__ = 'sergiojune'
from datetime import datetime, timedelta, timezone
import re

# 获取现在时间
dt = datetime.now()
print(dt)
print(type(dt))

# 获取指定某日的时间，即是创建实例
ddt = datetime(2017, 10, 15, 12, 35, 56)
print(ddt)  # 类型为datetime.datetime

# 将datetime转为timestamp
ts = dt.timestamp()
print(ts)
print(type(ts))  # 类型为float
# 将timestamp转为datetime
d = datetime.fromtimestamp(ts)
print(d)
# 将timestamp转为标准的utc时间,比北京时间少了八小时
d = datetime.utcfromtimestamp(ts)
print(d)

# 将字符串转为时间
s = '2017:12:12 11:11:11'
sd = datetime.strptime(s, '%Y:%m:%d %H:%M:%S')  # 第二个参数为字符串的时间格式
print(sd)
print(type(sd))

# 将时间转为字符串,参数为转为字符串的格式
ds = sd.strftime('%Y:%m:%d %H:%M:%S')
print(ds)
print(type(ds))


# 将时间进行加减
print('之前：', dt)
dt = dt + timedelta(hours=5,minutes=25)
print(dt)
dt = dt + timedelta(days=5)
print(dt)

print('-------------------')
# 将本地datetime设一个时区
tz_local = timezone(timedelta(hours=8))
d = datetime.now()
print(d)
# 强行设置时区,tzinfo就是时区信息
now = d.replace(tzinfo=tz_local)
print(now)

print('----------------------')
# 时区时间任意转换
# 拿到utc时间,并设置时区
d = datetime.utcnow().replace(tzinfo=timezone.utc)
print(d)
# 转为北京时间的时区
bj_utc = d.astimezone(tz=timezone(timedelta(hours=8)))
print(bj_utc)
# 转为东京时间
dj_utc = d.astimezone(tz=timezone(timedelta(hours=9)))
print(dj_utc)
# 也可以直接利用北京时间转为东京时间
dj_utc = bj_utc.astimezone(tz=timezone(timedelta(hours=9)))
print(dj_utc)
# 所以用astimezone()这个方法可以任意转换时区


# 作业：假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp
def to_timestamp(time, tz):
    # 将字符串转为时间
    time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    # 设置该时间的时区
    time = time.replace(tzinfo=timezone(timedelta(hours=tz)))
    time = time.timestamp()
    return time


print('---------------')
time1 = '2015-6-1 08:10:30'
utc1 = 'UTC+7:00'
# 用正则匹配出时间
utc1 = int(re.search('UTC([+-][\d]{1,2}):[\d]{2}', utc1).group(1))
print(utc1)
time = to_timestamp(time1, utc1)
print(time)

time2 = '2015-5-31 16:10:30'
utc2 = 'UTC-09:00'
# 用正则匹配出时间
utc2 = int(re.search('UTC([+-][\d]{1,2}):[\d]{2}', utc2).group(1))
print(utc2)
time2 = to_timestamp(time2, utc2)
print(time2)
