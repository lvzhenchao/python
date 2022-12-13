
## Base64 是一种用64个字符来表示任意二进制数据的方法
### 二进制文件包含很多无法显示和打印的字符，记事本处理二进制数据，就需要一个二进制到字符串的转换方法。Base64是一种最常见的二进制编码方法

import base64

print(base64.b64encode(b'binary\x00string'))

print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

### 标准的Base64编码后可能出现字符+和/,在URL中就不能直接作为参数，所以又有一种 url safe 编码，其实就是把字符+和/分别变成-和_

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))

print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))

print(base64.urlsafe_b64decode('abcd--__'))

### base64 是一种通过查表的编码方法，不能用于加密，即时使用自定义的编码表也不行
### base64 适用于小段内容的编码，比如数字证书签名、Cookie的内容
### base64 算法是最早应用于解决电子邮件传输的问题，因为早期电子邮件只允许ASCll码字符，网关会对非ASCll码字符的二进制做调整
### base64 内容传送编码是一种以任意8位字节序列组合的描述形式；会比原始数据略长，为原来的4/3倍。编码后的字符串数是以4为单位的整数倍
