# Python 列表

"""
字符串
列表
元组
字典
"""


# List 用于存储一串信息
# 列表用 [] 定义，数据之间用 , （逗号）分隔
# 列表的索引从 0 开始

name_list = ["zhangsan","lisi","wangwu"]

len(列表)  # 获取列表长度 n+1
列表.count(数据)  # 数据在列表中出现的次数

列表.sort()   # 升序排序
列表.sort(reverse=True)  # 降序排序
列表.reverse()  # 反转/逆序

列表[索引]  # 从列表中取值
列表.index(数据)  # 获得数据第一次出现的索引

del 列表[索引]  # 删除指定索引的数据  （del关键字本质上是用来将一个变量从内存中删除）
列表.remove[数据]  # 删除第一个出现的指定数据
列表.pop  # 删除末尾数据
列表.pop(索引)  # 删除指定索引的数据

列表.insert(索引,数据)  # 在指定位置插入数据
列表.append(数据)  # 在末尾追加数据
列表.extend(列表2)  # 将列表2的数据追加到列表1


# 列表遍历
# 遍历就是从头到尾依次从列表中获取数据
# 在循环体内部针对每一个元素，执行相同的操作

# 顺序的从列表中依次获取数据，
# 每次循环过程中，
# 数据都会保存在 name 这个变量中，
# 在循环体内部可以访问到当前这一次获取到的数据
for name in name_list:
	
	循环内部针对列表元素进行操作
	print(name)



# 列表应用场景

# 列表 大多 存储相同类型的数据（可以存储不同类型的数据）













