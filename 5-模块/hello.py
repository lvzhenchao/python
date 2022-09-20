# 文档注释
'测试 module'

# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途
# 非公开的（private）
__author__ = 'lzc'

#导入该模块
import sys

def test():
	# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
	# python hello.py Michael获得的sys.argv就是['hello.py', 'Michael']
	args = sys.argv
	if len(args) == 1: 
		print('hello, world')
	elif len(args) == 2:
		print('hello, %s!' % args[1])
	else:
		print('Too many args')
		
# 命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__
if __name__ == '__main__':
	test()