# 变量前面如果加上__下划线，就会变成一个私有变量private,只能内部访问，外部不能访问

class Student(object):
	#定义一个特殊的__init__方法, 初始化方法
	#注意到__init__方法的第一个参数永远是self，表示创建的实例本身
	#参数必须传，但self不需要传
	def __init__(self, name, score):
		#self.name = name
		#self.score = score
		# 变成私有变量
		self.__name = name
		self.__score = score
		
	def get_name(self):
		return self.__name
		
	def get_score(self):
		return self.__score
		
	def print_score(self):
		#print('%s: %s' % (self.name, self.score))
		print('%s: %s' % (self.__name, self.__score))
		
	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'

bart = Student("lzc", 34)
lisa = Student("zhh", 100)

#print(bart.name)
#print(bart.score)

# 类的外部不能访问私有变量,下面两个变量不能被访问，不过可以通过自定义方法，get_name，get_score
# print(bart.__name)
# print(bart.__score)

print(bart.get_name())
print(bart.get_score())

bart.print_score()
print(bart.get_grade())
print(lisa.get_grade())

# 继承和多态
## 基类、父类、超类
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
	
dog = Dog()
print(isinstance(dog, Animal))# Animal的多态
print(dog.run())
print(dog.eat())
cat = Cat()
print(cat.run())

## 多态的展示
def run_twice(Animal):
	Animal.run()
	Animal.run()
print(run_twice(Animal()))
print(run_twice(Dog()))
print(run_twice(Cat()))


## 静态语言vs动态语言
### 对于静态（例如java）,必须要传入Animal类型或者它的子类，否则无法调用run()方法
### 对于动态语言，不一定需要传入Animal类型。只需要保证传入的对象有一个run方法即可
### 动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子

class Timer(object):
	def run(self):
		print("Start...")







































