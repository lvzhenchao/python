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
## 字典的items()可以同时迭代k,和v
for k,v in d.items():
	print(k, v)
	
##判断一个对象是否可迭代的：引入
from collections.abc import Iterable
### 判断字符串是否可迭代
print(isinstance('abc', Iterable))
### 判断list是否可迭代
print(isinstance([1,2,3], Iterable))
### 判断整数是否可迭代
print(isinstance(2, Iterable))

## 使用enumerate函数，将list变成索引-元素对
for k,v in enumerate(['a','b', 'c']):
	print(k,':', v)
	
for x,y in [(1,1), (2,4), (3,9)]:
	print(x,':',y)
	
## 列表生成器:直接创建一个列表
for x in range(1, 11):
	print(x * x)
### 方便
print([x*x for x in range(1, 11)])
### 列出文件和目录
import os
print([d for d in os.listdir('.')])


# 生成器：一边循环一边计算，减少内存占用
# 生成器函数和普通函数执行流程不一样，普通函数时顺序执行；
# 而变成生成器函数，是在每次调用next的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句继续执行
g = (x*x for x in range(10))
print(next(g))

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
g = odd()
next(g)
next(g)
next(g)

## 斐波拉契原生
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		print(b)
		a,b = b, a+b
		n = n+1
	return "done"
print(fib(6))

## 生成器：斐波拉契
import sys
def fibonacci(max): # 生成器函数 - 斐波那契
    n,a,b = 0,0,1
    while n < max:
        yield a
        a, b = b, a + b
        n = n+1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
		
## 迭代器


	































	
	


