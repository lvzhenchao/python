# 切片
list = ['lzc','zhh','lhy','lyc']
## 切片操作符
print(list[0:2])
print(list[1:2])
print(list[:1])

tuple = ('lzc','zhh','lhy','lyc')
print(tuple[0:2])
print(tuple[1:2])
print(tuple[:1])

string = "lzczhhlhylyc"
print(string[0:2])
print(string[1:2])
print(string[:1])
print(string[5:])

# 切片：循环遍历称为迭代
d = {'a':1, 'b':2, 'c':3}
## 下面迭代的是k
for k in d:
	print(k)
## 下面迭代的是value
for v in d.values():
	print(v)
##判断一个对象是否可迭代的
from collections.abc import Iterable
	
	


