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







































