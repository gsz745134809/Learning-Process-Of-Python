# 用元组的方式返回多个值


def measure():
	print("begin")
	temp = 37
	wetness = 50
	print("end")
	# 此时return可以同时返回temp和wetness的值 ，并且可以省略一对小括号
	return (temp,wetness)  # 可以写成 return temp,wetness


# 接收返回值时可以用多个变量接收
# 注意：使用多个变量接收结果时，变量的个数应该和元组中的元素的个数保持一致
gl_temp, gl_wetness = measure()




# 交换两个变量的值
a, b = (b, a)   # 交换变量a 和变量b 的值
# 并且小括号可以省略  
a, b = b, a  #等号右边是元组




'''
在函数内部使用方法修改可变参数会影响外部实参
'''
def mutable(num_list):
	
	num_list.extend([1,2,3])
	
	print(num_list)

gl_list = [6,7,8]
mutable(gl_list)
print(gl_list)




"""
关于 += 运算符
	在Python中，列表 变量调用 += 本质上是在执行列表变量的extend方法，不会修改变量的引用
	（但是列表变量使用 list_a = list_a + list_b 时，会修改变量的引用）
"""
def demo(num_list):
	num_list += num_list   # 此时会修改gl_list列表变量的引用
	print(num_list)
gl_list = [1,2,3]
print(gl_list)




"""
3.3、多值参数

定义支持多值参数的函数
	、有时可能需要一个函数能够处理的参数个数是不确定的，这个时候，就可以使用多值参数
	、Python中有两种多值参数：
		、参数名前增加一个 * 可以接收 元组
		、参数名前增加两个 * 可以接收 字典
	、一般在给多值参数命名时，习惯使用以下两个名字
		、*args --存放 元组 参数，前面有一个 *
		、**kwargs --存放 字典 参数，前面有两个 *
	、args 是 arguments 的缩写，有变量的含义
	、kw 是keyword 的缩写，kwargs可以记忆键值对参数
	
"""
def demo(num, *args, **kwargs):
	
	print(num)
	print(args)
	print(kwargs)

demo(1,2,3,4,5,name="小明", age=18,gender=True)


# 元组和字典的拆包
'''
在调用带有多值参数的函数时，如果希望：
	、将一个 元组变量，直接传递给 args
	、将一个 字典变量，直接传递给 kwargs
就可以使用 拆包，简化参数的传递，拆包的方式是：
	、在 元组变量前，增加 一个 *
	、在 字典变量前，增加 两个 *

'''
def demo(*args, **kwargs):
	
	print(args)
	print(kwargs)

# 需要将一个元组变量/字典变量传递给函数对应的参数
gl_nums = (1,2,3)
gl_xiaoming = {"name": "小明",
				"age": 18}

# 调用函数时，在元组变量前，增加 一个 *		
# 在 字典变量前，增加 两个 *
# 拆包语法		
demo(*gl_nums, **gl_xiaoming)