
## urllib提供了一系列操作URL的功能
### 可以非常方便地抓取URL内容，也就是发送一个GET请求，然后返回http的响应

from urllib import request

#with request.urlopen('https://www.baidu.com/') as f:
#	data = f.read()
#	print('Status:', f.status, f.reason)
#	for k, v in f.getheaders():
#		print('%s: %s' % (k, v))
#	print('Data:', data.decode('utf-8'))

from urllib import request

with request.urlopen('https://www.baidu.com/') as f:
	data = f.read()
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
	print('Data:', data.decode('utf-8'))