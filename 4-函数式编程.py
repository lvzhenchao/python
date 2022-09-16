# 函数式编程：抽象程度很高的编程范式；特点：允许把函数本身作为参数传入另一个函数，还允许返回一个函数
# 纯粹的函数式编程没有变量；
# python支持部分

## 高阶函数
### map() 一个函数，一个Iterable类型的数据;事实上它把运算规则抽象了
def f(x):
	return x * x
r = map(f, [1,2,3,4,5,6])
print(list(r))#Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list

### reduce


### filter() 一个函数，一个序列
def is_odd(n):#保留奇数
	return n%2 == 1
	
print(list(filter(is_odd, [1,2,3,4,5,6,7])))

### sorted() 排序
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key = abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

## 装饰器：在代码运行期间动态增加功能的方式

## 偏函数：就是把一个函数的参数给固定住（设置默认值，返回一个新的函数，调用这个新函数会更简单）
import functools
int2 = functools.partial(int, base=2)
print(int2('10000'))