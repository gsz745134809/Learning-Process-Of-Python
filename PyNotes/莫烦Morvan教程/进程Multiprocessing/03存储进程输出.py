'''
Queue的功能是将每个核或线程的运算结果放在队里中， 等到每个线程或核运行完毕后再从队列中取出结果， 
继续加载运算。原因很简单, 多线程调用的函数不能有返回值, 所以使用Queue存储多个线程运算的结果
'''


# 把结果放在 Queue 里 
# 定义一个被多线程调用的函数，q 就像一个队列，用来保存每次函数运行的结果

#该函数没有返回值！！！
def job(q):
    res=0
    for i in range(1000):
        res+=i+i**2+i**3
    q.put(res)    #queue


# 主函数 
# 定义一个多线程队列，用来存储结果
if __name__=='__main__':
    q = mp.Queue()

# 定义两个线程函数，用来处理同一个任务, args 的参数只要一个值的时候，
# 参数后面需要加一个逗号，表示args是可迭代的，后面可能还有别的参数，不加逗号会出错
p1 = mp.Process(target=job,args=(q,))
p2 = mp.Process(target=job,args=(q,))

# 分别启动、连接两个线程
p1.start()
p2.start()
p1.join()
p2.join()

# 上面是分两批处理的，所以这里分两批输出，将结果分别保存
res1 = q.get()
res2 = q.get()

# 打印最后的运算结果
print(res1+res2)


# 完整的代码 
import multiprocessing as mp

def job(q):
    res=0
    for i in range(1000):
        res+=i+i**2+i**3
    q.put(res)    #queue

if __name__=='__main__':
    q = mp.Queue()
    p1 = mp.Process(target=job,args=(q,))
    p2 = mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1+res2)

# 运行的时候还是要在terminal中，最后运行结果为
'''
499667166000
'''