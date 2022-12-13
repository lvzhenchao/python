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

## collections 提供了许多有用的集合类

### namedtuple是一个函数，用创建自定义tuple对象，并且规定了tuple元素的个数；可以方便地定义一种数据类型，具备tuple的不变性，又可以根据属性来引用
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))

### deque deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈;实现list的append()和pop()外，还支持appendleft()和popleft()
from collections import deque
q = deque(['a', 'b'])
q.append('x')
q.appendleft('y')
print(q)

### defaultdict 这个dict可以在key不存在的时候，返回默认值
from collections import defaultdict
dc = defaultdict(lambda: "N/A")
dc['key1'] = 'abc'
print(dc['key1'])
print(dc['key2'])

### OrderedDict 此函数是保持key顺序的dict
from collections import OrderedDict
dd = dict([('a', 1), ('b', 2), ('c', 3)])
print(dd)
print(dd)

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
od['f'] = 11
od['d'] = 12
od['e'] = 13
print(od) # 按照插入的顺序排列，不是key的本身排序


























































