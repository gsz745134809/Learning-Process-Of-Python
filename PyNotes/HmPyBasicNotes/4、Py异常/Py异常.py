
# 用 try(尝试) 来捕获异常
try:
	尝试执行的代码
except:
	出现错误的处理

# try 尝试，下方编写要尝试代码，不确定是否能够正确执行的代码
# except 如果不是，下方编写尝试失败的代码

try:
	# 提示用户输入一个数字
	num = int(input("请输入一个整数："))
except:
	print("请输入正确的整数")




# 错误类型捕获

try:
	# 尝试执行的代码
	pass
except 错误类型1:
	# 针对错误类型1，对应的代码处理
	pass
except 错误类型2:
	# 针对错误类型，对应的代码处理
	pass
except Exception as result:
	print("未知错误 %s " % result)


# 当Python解释器抛出异常时，最后一行错误信息的第一个单词，就是错误类型







# 异常捕获完整语法

try:
	# 尝试执行的代码
	pass
except 错误类型1:
	# 针对错误类型1，对应的代码处理
	pass
except 错误类型2:
	# 针对错误类型，对应的代码处理
	pass
except (错误类型3, 错误类型4):
	# 针对错误类型3 和4，对应的代码处理
except Exception as result:
	# 打印错误信息（针对未知错误类型）
	print(result) 
else:
	# 没有异常才会执行的代码
	pass
finally:
	# 无论是否有异常，都会执行的代码
	print("无论是否有异常，都会执行的代码")





# 异常的传递性






# 04、抛出raise异常
"""
例如：用户登录模块中，提示用户输入密码，如果长度少于8，主动抛出异常
"""

"""
4.2 抛出异常

。Python中提供了一个 Exception 异常类
。在开发时，如果满足特定业务需求时，希望抛出异常，可以：
	1、创建一个 Exception 的对象
	2、使用 raise 关键字 抛出 异常对象
"""

'''
需求
。定义 input_password 函数，提示用户输入密码
。如果用户输入长度 < 8 ，抛出异常
。如果用户输入长度 >=8 , 返回输入的密
'''

def input_password():
	
	# 1、提示用户输入密码
	pwd = input("请输入密码：")
	
	# 2、判断密码长度 >=8 ，返回用户输入的密码
	if len(pwd) >= 8:
		return pwd
	
	# 3、如果 <8 主动抛出异常
	print("主动抛出异常")
	
	# 1>创建异常对象 - 可以使用错误信息字符串作为参数
	ex = Exception("密码长度不够")
	# 2>主动抛出对象
	raise ex
	
	
# 提示用户输入密码
try:	
	print(input_password())
except Exception as result:
		print(result)
	



















