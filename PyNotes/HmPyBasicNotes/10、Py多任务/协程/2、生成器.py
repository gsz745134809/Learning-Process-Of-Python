# 1、生成器

'''
利用迭代器，我们可以在每次迭代获取数据（通过next()方法）时按照特定的规律进行生成。但是我们在实现了
一个迭代器时，关于当前迭代到的状态需要我们自己记录，进而才能根据当前状态生成下一个数据。为了达到
记录当前状态，并配合next()函数进行迭代使用，我们可以采用更简洁的语法，即生成器(generator)。
生成器是一类特殊的迭代器。
'''

# 2、创建生成器方法1
'''
要创建一个生成器，有很多中方法。第一种方法很简单，只要把一个列表生成式的[]改成()
'''
In [1]: L = [x*2 for x in range(5)]

In [2]: L
Out[2]: [0, 2, 4, 6, 8]

In [3]: G = (x*2 for x in range(5))

In [4]: G
Out[4]: <generator object <genexpr> at 0x000001B2C73FABA0>
'''
创建L和G的区别仅在于最外层的[]和()，L是一个列表，而G是一个生成器。我们可以直接打印出列表L的每一个元素，
而对于生成器G，我们可以按照迭代器的使用方法来使用，即可以通过next()函数、for循环、list()等方法使用。
'''


# 3、创建生成器方法2
'''
generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
'''
def create_num(all_num):
	# a = 0
	# b = 1
	a, b = 0, 1
	current_num = 0
	while current_num < all_num:
		# print(a)  # 用print直接打印出来 
		yield a  # 此处的a 给下面的num
		# 如果一个函数中有yield语句，那么这个就不是函数，而是一个生成器的模板  
		# 如果原本要append到列表中（占用空间），此时用yield声明a，说明这是一个生成器
		a, b = b, a+b
		current_num += 1
		
# 如果在调用create_num的时候，发现这个函数中有yield，那么此时不是调用函数，而是创建一个生成器对象
# create_num(10)
obj = create_num(10)  

for num in obj:  # 此处的num的值是从上面 yield a 的那个a中取
	print(num)





def create_num(all_num):
	print("----1----")
	a, b = 0, 1
	current_num = 0
	while current_num < all_num:
		print("----2----")  
		yield a 
		print("----3----")
		a, b = b, a+b
		current_num += 1
		print("----4----")

obj = create_num(10)

ret = next(obj)
print(ret)

ret = next(obj)
print(ret)

'''
输出：
----1----
----2----
0
----3----
----4----
----2----
1
'''
说明第一次调用next()从print("----1----")开始执行
第二次调用next()就直接从循环开始了（从上一次停止的地方开始执行，即yield a 那里）






# 想要得到一个生成器的返回值，如下
def create_num(all_num):
	a, b = 0, 1
	current_num = 0
	while current_num < all_num:
		yield a 
		a, b = b, a+b
		current_num += 1
	return "ok..."

obj = create_num(10)

while True:
	try:
		ret = next(obj)
		print(ret)
	except Exception as ret:
		print(ret.value)  # 此处得到函数create_num()函数的返回值
		break


  # 总结
  '''
  。使用了yield关键字的函数不再是函数，而是生成器。（使用了yield的函数就是生成器）
  。yield关键字有两点作用：
		、保存当前运行状态（断点），然后暂停执行，即将生成器（函数）挂起
		、将yield关键字后面表达式的值作为返回值返回，此时可以理解为起到了return的作用
  。可以使用next()函数让生成器从断点处继续执行，即唤醒生成器（函数）
  。Python3 中的生成器可以使用return返回最终运行的返回值，而Python2中的生成器不允许使用return返回一个值  
  '''




# 4、使用send唤醒
'''
我们除了可以使用next()函数来唤醒生成器继续执行外，还可以使用send()函数来唤醒执行。使用send()函数的一个
好处是可以在唤醒的同时向断点处传入一个附加数据。
'''

def create_num(all_num):
	a, b = 0, 1
	current_num = 0
	while current_num < all_num:
		ret = yield a 
		print(">>>ret>>>", ret)
		a, b = b, a+b 
		current_num +=1
obj = create_num(10)

# obj.send(None)  #send一般不会放到第一次启动生成器，如果非要这样做，那么传递None

ret = next(obj)
print(ret)

# send里面的数据会传递给 ret = yield a 中的 ret，当作yield a 的结果，然后ret保存这个结果
# send的结果是下一次调用yield时 ，yield 后面的值
ret = obj.send("hahaha")
print(ret)




















