# 常用内建模块

## datetime 是处理日期和时间的标准库

### 获取当前日期和时间
from datetime import datetime, timedelta
now = datetime.now()# 获取当前datetime
print(now)
print(type(now))

### 获取指定的日期和时间
dt = datetime(2022,11,18,15,46) # 指定日期时间创建datetime
print(dt)

### datetime转换timestamp (是一个浮点数，整数表示秒)
print(dt.timestamp())

### timestamp转换为datetime 
t = 1429417200.0
print(datetime.fromtimestamp(t))    # 本地时间
print(datetime.utcfromtimestamp(t)) # UTC时间

### str转换为datetime
cday = datetime.strptime('2015-6-1', '%Y-%m-%d')
print(cday)
### datetime转换为str
now1 = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
print(now.strftime('%Y-%m-%d %H:%M:%S'))

### datetime加减， 加减可以直接用+和-运算符，不过需要导入timedelta这个类
now2 =  now + timedelta(hours=10)
print(now2)
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))


