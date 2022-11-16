# 多任务可以由多进程完成，也可以由一个进程内的多线程完成
# 线程是操作系统直接支持的执行单元，Python的线程是真正的Posix Thread【就是POSIX的线程标准，定义了创建和操纵线程的一套API】，而不是模拟出来的线程

## 多线程能让你运行一个独立的程序一样运行一段长代码，有点像调用子进程，不过区别是调用【一个函数】或者【一个类】，而不是调用独立的程序；

# 标准库提供了两个模块：_thread[低级模块]和threading[高级模块：对低级模块进行了封装]；

import time, threading

# 新线程执行的代码
def loop():
	print('线程 %s 开始了...' % threading.current_thread().name)
	n = 0
	while n < 5:
		n = n + 1
		print('thread %s >>> %s' % (threading.current_thread().name, n))
		time.sleep(1)
	print('thread %s ended.' % threading.current_thread().name)
	
print('线程 %s 开始了...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

## 由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程
## current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫MainThread

# LOCK
## 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
## 多线程中，所有变量都由所有线程共享，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了

# 假定这是你的银行存款: 理论上结果应该为0，但是线程的调度是由操作系统决定
## 原因：高级语言的一条语句在CPU执行时是若干条语句，balance = balance + n，也分两步：计算balance + n，存入临时变量中；将临时变量的值赋给balance。
## x是局部变量，两个线程各自都有自己的x,t1和t2是交替运行的，执行这几条语句，线程可能中断，导致多个线程把同一个对象的内容改乱了

balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(2000000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

## 上锁
### 好处：锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行
### 坏处：首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止



























