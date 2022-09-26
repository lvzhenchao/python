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






































