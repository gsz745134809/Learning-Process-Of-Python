# gevent
'''
greenlet已经实现了协程，但是这个还得人工切换，python还有一个比greenlet更强大的并且能够自动切换任务的模块gevent

其原理是当一个greenlet遇到IO（指的是input output 输入输出，比如网络、文件操作等）操作时，比如访问网络，
就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。

由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO

pip install gevent
'''

import gevent

def f(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		gevent.sleep(0.5)  # 模拟一个耗时操作
		
g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)

g1.join()
g2.join()
g3.join()












from gevent import monkey
import gevent
import random
import time

# 有耗时操作时需要
monkey.patch_all()  # 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块


def coroutine_work(coroutine_name):
	for i in range(10):
		print(coroutine_name, i)
		time.sleep(random.random())
		
gevent.joinall([
		gevent.spawn(coroutine_work, "work1"),
		gevent.spawn(coroutine_work, "work2")
])




































