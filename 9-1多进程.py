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


## 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
	
    p = Process(target=run_proc, args=('test',))# 创建一个Process实例，只需要传入一个执行函数和函数的参数
	
    print('Child process will start.')
    p.start() # 方法启动
    p.join()  # 等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Child process end.')
	
## Pool 进程池，如果要启动大量的子进程，可以用进程池的方式批量创建子进程
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
	print('Run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name, (end - start)))
	
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p1 = Pool(4) # Pool的默认大小是CPU的核数
    for i in range(5):
        p1.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p1.close() # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    p1.join() # 调用join()方法会等待所有子进程执行完毕
    print('All subprocesses done.')
	
# 很多时候， 子进程并不是自身，而是一个外部进程，创建了子进程后，还需要控制子进程的输入和输出
## subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出
#import subprocess

#print('$ nslookup www.python.org')
#r = subprocess.call(['nslookup', 'www.python.org'])
#print('Exit code:', r)

## 进程间通信：Queue、Pipes等多种方式交换数据
print("---------------------------")

from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()




































 

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
