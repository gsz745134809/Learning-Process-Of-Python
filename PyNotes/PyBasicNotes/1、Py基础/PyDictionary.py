# dictionary（字典）是除列表以外Python之中最灵活的数据类型

# 字典用来存储多个数据，通常用于存储描述一个物体的相关信息

# 和列表的区别
	# 列表是 有序 的对象集合
	# 字典是 无序 的对象集合

# 字典用 {} 定义
# 字典使用 键值对 存储数据，键值对之间使用逗号,分隔
	# 键key 是索引
	# 值value 是数据
	# 键和值之间使用 : （冒号）分隔
	# 键必须是唯一的
	# 值可以取任何数据类型，但 键 只能使用字符串、数字或元组

xiaoming = {"name":"小明",
			"age":18,
			"gender":True,
			"height":1.75}



len(字典)  # 获取字典的 键值对数量

字典.keys()  # 所有key列表
字典.values()  # 所有value列表
字典.items()  # 所有(key,value)元组列表




# 遍历字典
# 遍历 就是依次从字典中获取所有键值对

# for 循环内部使用的 'key 的变量' in 字典

for k in xiaoming:
	
	print("%s: %s" % (k,xiaoming[k]))


"""
将多个字典放在一个列表中再进行遍历
"""

