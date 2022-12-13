
## 常见的摘要算法 MD5、SHA1等；摘要算法：又称哈希算法、散列算法。通过一个函数，把任意长度的数据转换为一个长度固定的数据串(通常用16进制的字符串表示)
## 摘要算法是一个单向函数, 计算容易，反推非常困难

import hashlib

### md5 生成结果是固定的128 bit/16字节，通常用一个32位的16进制字符串表示
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

#### 如果数据量很大，可以分块多次调用update()
md5_1 = hashlib.md5()
md5_1.update('how to use md5 in '.encode('utf-8'))
md5_1.update('python hashlib?'.encode('utf-8'))
print(md5_1.hexdigest())

### SHA1 结果是160 bit/20字节，通常用一个40位的16进制字符串表示
import hashlib

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

## hmac 盐值计算 
### hmac输出的长度和原始哈希算法的长度一致。需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes
import hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())