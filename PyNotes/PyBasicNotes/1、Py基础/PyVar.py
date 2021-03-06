"""
01、变量的引用
	、变量和数据都是保存在内存中的
	、在Python中函数的 参数传递 以及 返回值 都是靠 引用 传递的

1.1、引用的概念
	在Python中
	、变量 和 数据 是分开存储的
	、数据 保存在内存中的一个位置
	、变量 中保存着数据在内存中的地址
	、变量 中记录数据的地址，就叫做 引用
	、使用 id() 函数库查看变量中保存数据所在的 内存地址
	
	注意：如果变量已经被定义，当给一个变量赋值的时候，本质上是 修改了数据的引用
	、变量 不再 对之前的数据引用
	、变量 改为 对新赋值的数据引用

1.2、变量引用的示例
	在Python中，变量的名字类似于便签纸贴在数据上
	、定义一个整数变量a，并赋值为1（此时id(a)就是数字1存储的地址）
	、将变量a赋值为2（此时id(a)就是数字2存储的地址）
	、定义一个整数变量b，并且将变量a的值赋值给b（此时id(b)就是变量a代表的数字的地址）
	

02、可变和不可变类型
	、不可变类型，内存中的数据不允许被修改：
		、数字类型 int,bool,float,complex,long(2.x)
		、字符串 str
		、元组 tuple
	、可变类型，内存中的数据可以被修改：
		、列表 list
		、字典 dict
		
	注意：字典的key只能使用不可变类型的数据
	
	注意：
		1、可变类型的数据变化，是通过方法来实现的
		2、如果给一个可变类型的变量，赋值了一个新的数据，引用会修改
			、变量不再对之前的数据引用
			、变量改为对新赋值的数据的引用


hash()函数接收一个不可变类型的数据作为参数，返回结果是一个整数



"""