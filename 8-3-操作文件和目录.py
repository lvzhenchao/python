# 内置OS模块

import os

##操作系统
print(os.name)#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
##详细的系统详细:windows系统不提供
#print(os.uname())
#print(os.uenviron)

## 操作目录和文件

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
#os.path.join('E:/python', 'testdir')
# 然后创建一个目录:
os.mkdir('E:/python/testdir')
# 删掉一个目录:
#os.rmdir('E:/python/testdir')

# 对文件重命名
#os.rename('test.txt', 'test.py')
# 删掉文件
#os.remove('test.py')