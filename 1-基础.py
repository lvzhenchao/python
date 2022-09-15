
a = 100
if a >= 0:
    print(a)
else:
    print(-a)
	
# 多行字符串表示
print('''line1
... line2
... line3''')

## list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们
## list列表数据类型，list是一种有序的集合，可以随时添加和删除其中的元素
classmates = ['lzc', 'zhh', 'lhy', 'lyc']
print(classmates[0])
print(classmates[-1])
classmates.append('hhh')
classmates.insert(1, 'zzz')
classmates.pop(0)
print(classmates)
print(len(classmates))

## tuple 有序列表，也叫元组；一旦初始化，就不能修改；更安全，能用tuple的地方尽量用
## 没有追加方法append等，不管几个元素之间记得加逗号分隔
classmatesTuple = ('lzc', 'zhh')
print(classmatesTuple)

# 条件判断：冒号是结尾
age = 31
if age >= 18:
	print("成人")
else :
	print("未成年")
	
## 字符串不能直接和整数比较
s = 12 # input('birth：')
birth = int(s)
if birth < 2000:
	print("你还小")
else:
	print("你不小了")
	
# 循环 for in, while
names = ['lzc', 'zhh', 'lhy']
for name in names:
	print(name)
	
sum = 0
numList = [1,2,3,4,5]
for v in numList:
	sum = sum + v
print(sum)

print(list(range(10)))


# 字典数据类型 dict{} 键值对;查找极快，内存比较浪费
d = {'lzc': 98, 'zhh': 96}
print(d['lzc'])
print(d.get('zhh1', -1))
print(d.pop('zhh'))
print(d)

# set集合数据类型 一组key的集合，不存储value；key不能重复；可以做交集，并集等操作
s = set([1,2,3])
print(s)
s1 = set([1,2,3,4,5,5,5,5,6])# 自动过滤重复数据
print(s1)
## 交集
print(s&s1)
## 并集
print(s|s1)

























