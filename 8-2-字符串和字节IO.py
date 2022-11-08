# StringIO：在内存中读写str
## 要把str写入StringIO，我们需要先创建StringIO,像文件一样写入即可
from io import StringIO

f = StringIO()
f.write("hello")
f.write(" ")
f.write("lzc")
print(f.getvalue())

## 读取StringIO, 可以用一个str 初始化StringIO，像读取文件一样读取
f1 = StringIO('hello\n hi\n lzccc')
while True:
	s = f1.readline()
	if s == '':
		break
	print(s.strip())
	
# BytesIO操作, 可以用bytes初始化，然后像文件一样读取
from io import BytesIO
b = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(b.read())