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
else:
	print("没毛病")
finally:
    print('finally...')
print('END')
