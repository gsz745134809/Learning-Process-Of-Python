# 创建多进程 multiprocessing 

# 和上节一样，首先import multiprocessing并定义要实现的job()，同时为了容易比较，我们将计算的次数增加到1000000
import multiprocessing as mp

def job(q):
    res = 0
    for i in range(1000000):
        res += i + i**2 + i**3
    q.put(res) # queue


# 因为多进程是多核运算，所以我们将上节的多进程代码命名为multicore()
def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore:',res1 + res2)


# 创建多线程 multithread 

# 接下来创建多线程程序，创建多线程和多进程有很多相似的地方。首先import threading然后定义multithread()完成同样的任务
import threading as td

def multithread():
    q = mp.Queue() # thread可放入process同样的queue中
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread:', res1 + res2)


# 创建普通函数 

# 最后我们定义最普通的函数。注意，在上面例子中我们建立了两个进程或线程，均对job()进行了两次运算，所以在normal()中我们也让它循环两次
def normal():
    res = 0
    for _ in range(2):
        for i in range(1000000):
            res += i + i**2 + i**3
    print('normal:', res)

# 运行时间 

# 最后，为了对比各函数运行时间，我们需要import time， 然后依次运行定义好函数：
import time

if __name__ == '__main__':
    st = time.time()
    normal()
    st1 = time.time()
    print('normal time:', st1 - st)
    multithread()
    st2 = time.time()
    print('multithread time:', st2 - st1)
    multicore()
    print('multicore time:', time.time() - st2)

# 大功告成，下面我们来看下实际运行对比。

# 结果对比 
"""
# range(1000000)
('normal:', 499999666667166666000000L)
('normal time:', 1.1306169033050537)
('thread:', 499999666667166666000000L)
('multithread time:', 1.3054230213165283)
('multicore:', 499999666667166666000000L)
('multicore time:', 0.646507978439331)
"""

# 普通/多线程/多进程的运行时间分别是1.13，1.3和0.64秒。 我们发现多核/多进程最快，说明在同时间运行了多个任务。 而多线程的运行时间居然比什么都不做的程序还要慢一点，说明多线程还是有一定的短板的。 戳这里查看“多线程的短板是什么”。

# 我们将运算次数加十倍，再来看看三种方法的运行时间：

"""
# range(10000000)
('normal:', 4999999666666716666660000000L)
('normal time:', 40.041773080825806)
('thread:', 4999999666666716666660000000L)
('multithread time:', 41.777158975601196)
('multicore:', 4999999666666716666660000000L)
('multicore time:', 22.4337899684906)
"""
# 这次运行时间依然是 多进程 < 普通 < 多线程，由此我们可以清晰地看出哪种方法更有效率。