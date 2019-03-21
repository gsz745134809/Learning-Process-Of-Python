# 不加 join() 的结果 
# 我们让 T1 线程工作的耗时增加.
import threading
import time
def thread_job():
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1) # 任务间隔0.1s
    print("T1 finish\n")
added_thread = threading.Thread(target=thread_job, name='T1')
added_thread.start()
print("all done\n")

#预想中输出的结果是否为：
T1 start
T1 finish
all done
# 但实际却是：
T1 start
all done
T1 finish



# 加入 join() 的结果 
# 线程任务还未完成便输出all done。如果要遵循顺序，可以在启动线程后对它调用join：
added_thread.start()
added_thread.join()
print("all done\n")

# 使用join对控制多个线程的执行顺序非常关键。举个例子，假设我们现在再加一个线程T2，T2的任务量较小，会比T1更快完成：

def T1_job():
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")
def T2_job():
    print("T2 start\n")
    print("T2 finish\n")
thread_1 = threading.Thread(target=T1_job, name='T1')
thread_2 = threading.Thread(target=T2_job, name='T2')
thread_1.start() # 开启T1
thread_2.start() # 开启T2
print("all done\n")

# 输出的”一种”结果是：

T1 start
T2 start
T2 finish
all done
T1 finish

# 现在T1和T2都没有join，注意这里说”一种”是因为all done的出现完全取决于两个线程的执行速度， 完全有可能T2 finish出现在all done之后。这种杂乱的执行方式是我们不能忍受的，因此要使用join加以控制。

# 我们试试在T1启动后，T2启动前加上thread_1.join():

thread_1.start()
thread_1.join() # notice the difference!
thread_2.start()
print("all done\n")

# 输出结果：

T1 start
T1 finish
T2 start
all done
T2 finish

#可以看到，T2会等待T1结束后才开始运行。

# 如果我们在T2启动后放上thread_1.join()会怎么样呢？

thread_1.start()
thread_2.start()
thread_1.join() # notice the difference!
print("all done\n")

# 输出结果：

T1 start
T2 start
T2 finish
T1 finish
all done
# T2在T1之后启动，并且因为T2任务量小会在T1之前完成；而T1也因为加了join，all done在它完成后才显示。

# 你也可以添加thread_2.join()进行尝试，但为了规避不必要的麻烦，推荐如下这种1221的V型排布：

thread_1.start() # start T1
thread_2.start() # start T2
thread_2.join() # join for T2
thread_1.join() # join for T1
print("all done\n")

"""
T1 start
T2 start
T2 finish
T1 finish
all done
"""