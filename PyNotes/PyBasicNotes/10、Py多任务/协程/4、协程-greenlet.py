# greenlet 
'''
为了更好使用协程来完成多任务，python中的greenlet模块对其封装，从而使得切换任务变得更加简单

sudo pip install greenlet

''' 
from greenlet import greenlet
import time

def t1():
	while True:
		print("---A---")
		gr2.switch()
		time.sleep(0.5)
		
def t2():
	while True:
		print("---B---")
		gr1.switch()
		time.sleep(0.5)
	
gr1 = greenlet(t1)
gr2 = greenlet(t2)

# 切换到gr1中运行
gr1.switch()











