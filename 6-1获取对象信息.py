#获取对象信息
## 基本类型都可以用type判断
print(type(123))
print(type('str'))
print(type(None))

print(type(abs))


## 判断一个对象是否是函数，types模块中定义的常量
import types

def fn():
	pass

print(type(fn))
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

## 判断class的类型，使用isinstance()函数
## 继承关系 object->Animal->Dog->Husky 
class Animal(object):
	def run(self):
		print('Animal is running...')
		
## 子类继承父类
class Dog(Animal):
	def run(self):
		print('Dog is running')
	def eat(self):
		print('Dog eating meat')
class Cat(Animal):
	def run(self):
		print('Cat is running')
		
a = Animal()
d = Dog()
print("d是Dog的实例化：",isinstance(d, Dog))
print("d是Animal的实例化：",isinstance(d, Animal))

## 能用type()判断的基本类型也可以用isinstance()判断
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

## 判断一个变量是否是某些类型中的一种
print(isinstance([1,2,3], (list, tuple)))
print(isinstance((1,2,3), (list, tuple)))

## 获得一个对象的所有属性和方法，可以使用dir()函数
# print(dir(Dog))
print(dir('ABC'))
print(len('ABC'))

## __XXX__的属性和方法在python中都是有特殊用途的


























