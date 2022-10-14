# 定义了一个class后，可以给改实例绑定【任何属性和方法】，动态语言的灵活性
class Student(object):
	pass
	
	
s = Student()
## 给实例绑定一个属性
s.name = "lzc"
print(s.name)

## 绑定一个方法
def set_age(self, age):
	self.age = age
	
from types import MethodType
s.set_age = MethodType(set_age, s)# 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print(s.age)

### 给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
# s2.set_age(35)
# print(s2.age)

## 给所有实例绑定方法
def set_score(self, score):
	self.score = score
Student.set_score = set_score

s3 = Student()
s3.set_score(99)	
print(s3.score)


# __slots__限制实例的属性；比如只允许对Student实例添加name和age属性
## 仅对当前实例起作用，继承的子类不起作用

class StudentNew(object):
	__slots__ = ('name', 'age')  #只允许tuple定义允许绑定的属性名称
	
ss = StudentNew()
ss.name = "lll"
ss.age  = 13
#ss.score = 98 # AttributeError: 'StudentNew' object has no attribute 'score'

# 使用@property装饰器，把一个方法变成属性调用
## 为了防止属性暴露，防止随便改，没办法检查参数
## @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性
class Student1(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student1()
s.set_score(59)
s.get_score

class Student2(object):

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value
		
	@property
	def birth(self):
		return self._birth
	
	@birth.setter
	def birth(self, value):
		self._birth = value
		
	#只读属性，只定义getter方法，不定义setter方法就是一个只读属性
	@property
	def age(self):
		return 2022 - self._birth
		
s2 = Student2()
s2.score = 30
s2.score

# 多重继承:一个子类就可以同时获得多个父类的所有功能
## python 自带很多库使用了MixLn；
## 例如：TCPServer和UDPServer这两类网络服务
## 例如：ForkingMixIn和ThreadingMixIn多进程或多线程模型
## 不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类
class Animal(object):
    pass
	
### 新增跑功能
class RunnableMixIn(object):
    def run(self):
        print('Running...')
### 新增飞功能
class FlyableMixIn(object):
    def fly(self):
        print('Flying...')
### 肉食动物
class CarnivorousMixIn(object):
	def eat(self):
		print('eat meat...')
### 素食动物
class HerbivoresMixIn(object):
	def eat(self):
		print('eat glass...')
### 大类:
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
### 各种动物:
class Dog(Mammal):
    pass
## 需要飞功能的，就多继承一个Flyable，多重继承
class Bat(Mammal, FlyableMixIn):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

bat = Bat()
bat.fly()

# 定制类：类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的
## __slots__是为了控制类的属性，__len__方法为了让class作用于len()函数
## __str__：特殊打印控制；打印出来的实例，不但好看，而且容易看出实例内部重要的数据
class Student3(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student object (name: %s)' % self.name
	__repr__ = __str__# 增加一个这个就可以调试偷懒模式
	
print(Student3('lzc'))# <__main__.Student3 object at 0x0000016F308638B0>,打印出的不好看
### 增加了__str__之后，打印的就比较好看了

s3 = Student3("lzc123")
print(s3)
### __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是__repr__是为调试服务的
### __repr__ = __str__；通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法

## __iter__()方法，返回一个迭代对象；python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，知道遇到StopIteration错误时退出循环
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1# 初始化两个计数器a, b
	def __iter__(self):
		return self # 实例本身就是迭代对象，故返回自己
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b 
		if self.a > 100:
			raise StopIteration()
		return self.a
		
for n in Fib():
	print(n)
	
## __getitem__ 可以像list那样按照下标取出元素
class Fib1(object):
	def __init__(self):
		self.a, self.b = 0, 1# 初始化两个计数器a, b
	def __iter__(self):
		return self # 实例本身就是迭代对象，故返回自己
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b 
		if self.a > 100:
			raise StopIteration()
		return self.a
	def __getitem__(self, n):
		a, b = 1,1
		for x in range(n):
			a,b = b, a + b
		return a

f = Fib1()
print(f[2])
print(f[3])
print(f[4])
print(f[5])

## __getattr__调用不存在的方法或属性时
class Student4(object):
	def __init__(self):
		self.name = "lzc"
		
	def __getattr__(self, attr):
		if attr == 'score':
			return 99
		elif attr == 'age':
			return 18
s4 = Student4()
print(s4.name)
print(s4.score)
print(s4.age)

## 可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段
## 作用就是，可以针对完全动态的情况作调用。
## 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。

## 利用完全动态的__getattr__，我们可以写出一个链式调用：
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__
print(Chain().status.user.timeline.list)

## __call__添加一个方法，就可以直接对实例进行调用,调用自己本身
class Student5(object):
	def __init__(self, name):
		self.name = name
	def __call__(self):
		print('My name is %s.' % self.name)
s5 = Student5("lzc")
s5()

# 枚举类
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
	
from enum import Enum, unique
@unique # 装饰器可以帮助我们检查保证没有重复值
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
print(Weekday.Mon)

# 元类
print(type(Student5))
print(type(s5))
## type()函数既可以返回一个对象的类型，又可以创建出新的类型，需要传入3个参数
### 1、class的名称；
### 2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
### 3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
def fn(self, name="world"): #先定义函数
	print("Hello, %s." % name)
Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

## metaclass元类

	





































