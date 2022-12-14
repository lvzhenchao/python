# 正则
## \d：匹配一个数字
## \w：匹配一个字母或数字
## . 可以匹配任意字符
## 变长的字符：* 表示任意个字符，+ 表示至少一个字符，? 表示0个或一个字符，{n}表示n个字符，{n,m}表示n-m个字符

## \d{3}\s+\d{3,8}
### \d{3}表示匹配3个数字
### \s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格
### \d{3,8}表示3-8个数字

## 进阶： 做更精确地匹配，可以用[]表示范围
### [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线
### [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等
### [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串
### [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）
### A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'
### ^表示行的开头，^\d表示必须以数字开头
### $表示行的结束，\d$表示必须以数字结束

# re模块：包含所有正则表达式的功能
## s = 'ABC\\-001' # Python的字符串；对应的'ABC\-001'
## 使用Python的r前缀，就不用考虑转义的问题了：s = r'ABC\-001' # Python的字符串；'ABC\-001'

import re
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))# 匹配成功的返回一个Match对象
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))# 匹配不成功返回None

# 切分字符串：正则表达式切分字符串比用固定的字符串更灵活
print("a b  c".split(" "))

print(re.split(r"\s+", "a b  c"))

print(re.split(r'[\s\,]+', 'a,b, c  d'))

print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))

# 分组：除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）
## ^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码
## 可以在Match对象上用group()方法提取出子串
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))


# 贪婪匹配：正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符

## 示例，匹配出数字后面的 0 
print(re.match(r'^(\d+)(0*)$', '102300').groups()) # \d+ 采用贪婪匹配，直接把后面的0全部匹配，结果0*只能匹配空字符串了

## 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配
print(re.match(r'^(\d+?)(0*)$', '102300').groups())


# 编译




























