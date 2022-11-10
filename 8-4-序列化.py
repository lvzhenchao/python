# 程序运行过程中，所有变量都是在内存中；我们把变量从内存变成可传输的过程称之为序列化
import pickle

d = dict(name = 'lzc', age = 20, score = 99)
print(pickle.dumps(d))# 把任意对象序列化成bytes

## 另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f1 = open('dump.txt', 'rb')
d1 = pickle.load(f1)
f1.close()
print(d1)

## JSON
import json
d2 = dict(name = 'zhh', age = 20)
print(json.dumps(d2))
### dump()方法可以直接把JSON写入一个file-like Object

### JSON反序列化为Python对象，用loads()或者对应的load()方法
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))