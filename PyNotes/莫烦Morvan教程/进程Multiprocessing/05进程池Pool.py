# 这次我们讲进程池Pool。 进程池就是我们将所要运行的东西，放到池子里，Python会自行解决多进程的问题

# 首先 import multiprocessing 和定义 job()
import multiprocessing as mp

def job(x):
    return x*x


# 进程池 Pool() 和 map() 

# 然后我们定义一个Pool
pool = mp.Pool()

# 有了池子之后，就可以让池子对应某一个函数，我们向池子里丢数据，池子就会返回函数返回的值。 Pool和之前的Process的不同点是丢向Pool的函数有返回值，而Process的没有返回值。

# 接下来用map()获取结果，在map()中需要放入函数和需要迭代运算的值，然后它会自动分配给CPU核，返回结果
res = pool.map(job, range(10))

# 让我们来运行一下
def multicore():
    pool = mp.Pool()
    res = pool.map(job, range(10))
    print(res)
    
if __name__ == '__main__':
    multicore()

# 运行结果：
'''
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
'''


# 自定义核数量 

# 我们怎么知道Pool是否真的调用了多个核呢？我们可以把迭代次数增大些，然后打开CPU负载看下CPU运行情况

	# 打开CPU负载(Mac)：活动监视器 > CPU > CPU负载(单击一下即可)

# Pool默认大小是CPU的核数，我们也可以通过在Pool中传入processes参数即可自定义需要的核数量，
def multicore():
    pool = mp.Pool(processes=3) # 定义CPU核数量为3
    res = pool.map(job, range(10))
    print(res)


# apply_async() 

# Pool除了map()外，还有可以返回结果的方式，那就是apply_async().

# apply_async()中只能传递一个值，它只会放入一个核进行运算，但是传入值时要注意是可迭代的，所以在传入值后需要加逗号, 同时需要用get()方法获取返回值
def multicore():
    pool = mp.Pool() 
    res = pool.map(job, range(10))
    print(res)
    res = pool.apply_async(job, (2,))
    # 用get获得结果
    print(res.get())

# 运行结果；
'''
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]  # map()
4 # apply_async()
'''


# 用 apply_async() 输出多个结果 

# 那么如何用apply_async()输出多个迭代呢？

# 我们在apply_async()中多传入几个值试试
res = pool.apply_async(job, (2,3,4,))

# 结果会报错：
TypeError: job() takes exactly 1 argument (3 given)

# 即apply_async()只能输入一组参数。

# 在此我们将apply_async() 放入迭代器中，定义一个新的multi_res
multi_res = [pool.apply_async(job, (i,)) for i in range(10)]

# 同样在取出值时需要一个一个取出来
print([res.get() for res in multi_res])

# 合并代码
def multicore():
    pool = mp.Pool() 
    res = pool.map(job, range(10))
    print(res)
    res = pool.apply_async(job, (2,))
    # 用get获得结果
    print(res.get())
    # 迭代器，i=0时apply一次，i=1时apply一次等等
    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    # 从迭代器中取出
    print([res.get() for res in multi_res])

# 运行结果
'''
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81] # map()
4 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81] # multi_res
'''
# 可以看出在apply用迭代器的得到的结果和用map得到的结果是一样的

# # 总结 
1、Pool默认调用是CPU的核数，传入processes参数可自定义CPU核数
2、map() 放入迭代参数，返回多个结果
3、apply_async()只能放入一组参数，并返回一个结果，如果想得到map()的效果需要通过迭代