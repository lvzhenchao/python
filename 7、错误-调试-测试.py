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
