# zip 
# zip函数接受任意多个（包括0个和1个）序列作为参数，合并后返回一个tuple列表,请看示例：

a=[1,2,3]
b=[4,5,6]
ab=zip(a,b)
print(list(ab))  #需要加list来可视化这个功能
"""
[(1, 4), (2, 5), (3, 6)]
"""

# zip 中的运算

a=[1,2,3]
b=[4,5,6]
ab=zip(a,b)
print(list(ab))
for i,j in zip(a,b):
     print(i/2,j*2)
"""
0.5 8
1.0 10
1.5 12
"""


# lambda 
# lambda定义一个简单的函数，实现简化代码的功能，看代码会更好理解。

fun = lambda x,y : x+y, 冒号前的x,y为自变量，冒号后x+y为具体运算。

fun= lambda x,y:x+y
x=int(input('x='))    #这里要定义int整数，否则会默认为字符串
y=int(input('y='))
print(fun(x,y))

"""
x=6
y=6
12
"""


# map 
# map是把函数和参数绑定在一起。

>>> def fun(x,y):
	return (x+y)
>>> list(map(fun,[1],[2]))
"""
[3]
"""
>>> list(map(fun,[1,2],[3,4]))
"""
[4,6]
"""