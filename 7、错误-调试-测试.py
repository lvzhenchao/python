# 错误处理 try...except...fianlly...
try:
	print("try...")
	r = 10 / 0
	print("result:", r) # 当错误发生时，这行则不会被执行
except ZeroDivisionError as e: # 错误处理代码，执行完except后，如果有finally语句块，则执行finally语句块
	print('except:', e)
finally:
	print('finanlly...')
print('END')

## 可以用多个except语句块处理
try:
    print('try...')
    #r = 10 / int('a')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else: # 当没有错误发生时，会自动执行else语句
	print("没毛病")
finally:
    print('finally...')
print('END')

# 记录错误：内置的logging模块可以非常容易地记录错误信息
import logging
def foo(s):
	return 10 / int(s)
def bar(s):
	return foo(s) * 2
def main():
	try:
		bar("1")
	except Exception as e:
		logging.exception(e)
main()
print("loggin 测试完毕")

## raise错误
def foo1(s):
	n = int(s)
	if n == 0:
		raise ValueError("非法数据")
	return 10 / n
foo1(3)

## 添加到try
def bar1():
	try:
		foo1(0)
	except ValueError as e:
		print("ValueError!!!")
		raise # 语句如果不带参数，就会把当前错误原样抛出
bar1()

































