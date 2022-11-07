# IO在计算机中Input/Output, 也就是输入和输出；由于程序和运行时数据是在内存中中驻留，由CPU这个超快的计算核心来执行，涉及到数据交换的地方，通常是磁盘，网络等，就需要IO接口
# Stream 流是一个很重要的概念，Input Stream就是数据从外面（磁盘、网络）流进内存，Output Stream就是数据从内存流到外面去。
# IO编程中，就存在速度严重不匹配的问题；例如：比如把100M数据写入磁盘，CPU输出完只需要0.01秒，可磁盘接收需要10秒，两种办法：
## 1、CPU等着，也就是程序暂停执行后续代码，等100M的数据在10秒后写入磁盘；这种模式被称为【同步IO】
## 2、CPU不等待，只是告诉磁盘，慢慢写，后续代码可以立刻执行；这种模式被称为【异步IO】

### 异步IO的性能会远远高于同步IO，但是缺点是编程模型复杂；
#### 比如说等“汉堡”，而通知你的方法也各不相同。如果是服务员跑过来找到你，这是【回调模式】，如果服务员发短信通知你，你就得不停地检查手机，这是【轮询模式】


# 文件读写

## 读文件 open()函数，传入文件名和标示符
f = open('./test.txt', 'r')
## 把文件内容读到内存 read()
print(f.read());
##关闭文件，使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
f.close()

## 文件读写可能产生IOError, 一旦出错，f.close 就不会调用
try:
    f1 = open('./test.txt', 'r')
    print(f1.read())
finally:
    if f1:
        f1.close()

## 更简单的方法,不必调用f.close()方法
with open('./test.txt', 'r') as f2:
	print(f2.read())

## 防止文件过大，内存爆掉；需要反复调用read(size)方法，每次最多读取size个字节；readline()可以每次读取一行内容；readlines()一次读取所有内容并按行返回list
## 按需使用

## 像open()函数返回的这种有个read()方法的对象，叫做file-like Object；open方法除了file外，还可以是内存的字节流，网络流，自定义流等

## 二进制文件 rb模式
#f3 = open('./test.jpg', 'rb')
#print(f3.read())
#f3.close()

## 字符编码
f4 = open('./test.txt', 'r', encoding='gbk', errors='ignore')
print(f4.read())
f4.close()

## 写文件
#f5 = open('./test.txt', 'w')
f5 = open('./test.txt', 'a')
f5.write("lvzhenchao123")
f5.close()

#with open('/test.txt', 'a') as f6:
#    f6.write('Hello, world!')






















