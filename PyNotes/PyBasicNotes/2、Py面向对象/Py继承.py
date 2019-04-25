# 继承

class 类名(父类名):
	pass





# 重写中对父类方法的扩展
"""
1、在子类中重写父类的方法
2、在需要的位置使用 super().父类方法 来调用父类方法的执行
3、代码其他的位置针对子类的需求，编写 子类特有的代码实现

关于super
、在Python中 super是一个特殊的类
、super() 就是使用super类创建出来的对象
、最常使用的场景就是在重写父类方法时，调用 在父类中封装的方法实现

"""
class Dog():
	def bark(self):
		print("汪汪汪")

class XiaoTianQuan(Dog):
	def bark(self):
		# 1、针对子类特有的需求，编写代码
		print("神一样的叫唤...")
		# 2、使用 super(). 调用原本在父类中封装的方法
		super().bark()
		# 3、还可以增加其他子类的代码
		print("asfgdhrws")
xtq = XiaoTianQuan()
xtq.bark()





# 多继承
class 子类名(父类名1, 父类名2...):
	pass

# 应避免父类中出现相同名的属性或方法
# MRO方法搜索顺序
