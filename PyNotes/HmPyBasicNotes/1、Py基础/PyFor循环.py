
# 在Python中完整的for循环的语法如下：

for 变量 in 集合:
	
	循环体代码
else:
	没有通过break退出循环，循环结束后，会执行的代码


# 应用场景

# 在 迭代遍历 嵌套的数据类型时，例如 一个列表包含了多个字典
# 需求：要判断 某一个字典中 是否存在 指定的 值
	# 如果 存在， 提示并且退出循环
	# 如果 不存在， 在 循环整体结束 后，希望 得到一个统一的提示

students = [
		{"name": "阿土",
		"age": 20,
		"gender": True,
		"height": 1.7,
		"weight": 75.0},
		{"name": "小美",
		"age": 19,
		"gender": False,
		"height": 1.6,
		"weight": 45.0}
]

find_name = "阿土"

for stu_dict in students:
	
	print(stu_dict)
	
	if stu_dict["name"] == find_name:
	
		print("找到了 %s" % find_name)
		
		break

else:
	# 如果要找张三，会找不到，并且会在循环遍历完成之后执行下方语句
	print("没找到 %s" % find_name)

print("循环结束")











