print(abs(100))
print(abs(-100))

print(123.2)
print(int(123.3))
print(float(123))
print(str(123))


# 自定义函数 def语句
def my_abs(x):
	# 对参数进行类型检测
	if not isinstance(x, (int, float)):
		raise TypeError("数据类型错误，必须是数字类型")
	
	if x >= 0:
		return "大于等于0"
	else:
		return "小于0"
print(my_abs(1))
print(my_abs(-1))

## 空函数 pass语句
def nop():
	pass
## 实际上pass可以用来作为占位符， 还没想好怎么写函数的代码
age = 12
if age >= 18:
	pass
	
## return可以返回多个值
