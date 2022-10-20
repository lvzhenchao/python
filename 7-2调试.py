# 调试

## 第一种：print(),把可能有问题的变量打印出来看看，执行后在输出中查找打印的变量值
### print最大的坏处是将来还得删除掉它

## 第二种：断言 assert；启动Python解释器时可以用-O参数来关闭assert
def foo(s):
	n = int(s)
	assert n != 0, "n不能是0"   # 如果n不等于0，继续往下执行；
	return 10 / n

def main():
	foo(1)
main()

## 第三种：logging 可以输出到文件
import logging

s = '1'
n = int(s)
logging.info('n = %d' % n)
logging.basicConfig(level = logging.INFO)
print(10 / n)

## pdb 启动python的调试器pdb，让程序已单步运行，随时查看运行状态




























