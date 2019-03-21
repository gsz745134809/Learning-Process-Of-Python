# 添加线程 
# 本节我们来学习threading模块的一些基本操作，如获取线程数，添加线程等。首先别忘了
# 导入模块：
import threading


# 获取已激活的线程数
threading.active_count()
# 2


# 查看所有线程信息
threading.enumerate()
# [<_MainThread(MainThread, started 140736011932608)>, <Thread(SockThread, started daemon 123145376751616)>]
# 输出的结果是一个<_MainThread(...)>带多个<Thread(...)>。


# 查看现在正在运行的线程
threading.current_thread()
# <_MainThread(MainThread, started 140736011932608)>


# 添加线程，threading.Thread()接收参数target代表这个线程要完成的任务，需自行定义
def thread_job():
    print('This is a thread of %s' % threading.current_thread())
def main():
    thread = threading.Thread(target=thread_job,)   # 定义线程 
    thread.start()  # 让线程开始工作
if __name__ == '__main__':
    main()