# 单核CPU也可以执行多任务，操作系统轮流让各个任务交替执行

# 真正的并行执行多任务只能在多核CPU上执行，任务数量远多于CPU的核心数量，操作系统也会自动把多任务轮流调度到每个核心上执行

## 一个任务就是一个进程Process:
### 比如打开一个浏览器就是启动一个浏览器进程，打开一个记事本就启动了一个记事本进程，打开两个记事本就启动了两个记事本进程，打开一个Word就启动了一个Word进程
### 有些进程还不止同时干一件事，比如Word，它可以同时进行打字、拼写检查、打印等事情。在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）
### 一个进程至少一个线程；多个线程，可以同时执行，多线程的执行方式和多进程是一样的，也是由操作系统在多个线程之间快速切换，短暂交替运行

#多任务的实现有3种方式
## 多进程模式
## 多线程模式
##多进程+多线程模式【这种模型更复杂，实际很少采用】

## Unix/Linux 操作系统提供了一个fork()系统调用，非常特殊。普通函数可以调用，调用一次返回一次。但是fork()调用一次，返回两次，因为操作系统自动把当前进程（父进程）复制了一份（子进程），然后在父进程和子进程内返回
## 子进程永远返回0，而父进程返回子进程的ID；这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
import os

#print('Process (%s) start...' % os.getpid())

## Only works on Unix/Linux/Mac:
#pid = os.fork()
#if pid == 0:
#	print('子进程 (%s) and 父进程 is %s.' % (os.getpid(), os.getppid()))
#else:
#	print('我(%s)创建了一个子进程 (%s).' % (os.getpid(), pid))
	
# multiprocessing 跨平台的多进程模块：提供了一个Process类来代表一个进程对象
from multiprocessing import Process


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
	
    p = Process(target=run_proc, args=('test',))# 创建一个Process实例
	
    print('Child process will start.')
    p.start() # 方法启动
    p.join()  # 等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Child process end.')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
