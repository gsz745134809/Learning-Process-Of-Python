# 字符串就是一串字符，是编程语言中表示文本的数据类型

# 在Python中可以使用一对双引号" 或者一对单引号' 定义一个字符串

# 可以用for 循环遍历字符串中每一个字符

string = "Hello Python"

for c in string:
	print(c)



len(字符串)  # 获取字符串 长度
字符串_1.count(字符串_2)  # 字符串_2在字符串_1中出现的次数

字符串[索引]  # 从字符串中取出单个字符
字符串_1.index(字符串_2)  # 获得字符串_2第一次出现的索引




# 1、判断类型
string.isalnum()	如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回False
string.isalpha()	如果 string 至少有一个字符并且所有字符都是字母则返回True,否则返回False
*string.isdecimal()	如果 string 只包含十进制数字则返回 True 否则返回 False.
string.isdigit()	如果 string 只包含数字则返回 True 否则返回 False.
string.isnumeric()	如果string中只包含数字字符，则返回True，否则返回False
string.isspace()	如果 string 中只包含空格，则返回 True，否则返回 False.
string.istitle()	如果 string 是标题化的(见 title())则返回 True，否则返回 False
string.isupper()	如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
string.islower()	如果string中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回True，否则返回False


# 2、查找和替换
string.startswith(obj, beg=0,end=len(string))	检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.
string.endswith(obj, beg=0, end=len(string))	检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
string.find(str, beg=0, end=len(string))	检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
string.rfind(str, beg=0,end=len(string))	类似于find()函数，不过是从右边开始查找.
string.index(str, beg=0, end=len(string))	跟find()方法一样，只不过如果str不在 string中会报一个异常.
string.rindex( str, beg=0,end=len(string))	类似于 index()，不过是从右边开始.
string.replace(str1, str2, num=string.count(str1))	把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.（不会修改原有字符串内容）


# 3、大小写转换
string.capitalize()	把字符串的第一个字符大写
string.title()	返回"标题化"的string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
string.lower()	转换 string 中所有大写字符为小写.
string.upper()	转换 string 中的小写字母为大写
string.swapcase()	翻转 string 中的大小写


# 4、文本对齐
string.ljust(width)	返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
string.rjust(width)	返回一个原字符串右对齐,并使用空格填充至长度width的新字符串
string.center(width)	返回一个原字符串居中,并使用空格填充至长度width的新字符串


# 5、去除空白字符
string.lstrip()	截掉 string 左边的空白字符
string.rstrip()	删除 string 字符串末尾的空白字符.
*string.strip([obj])	在 string 上执行 lstrip()和 rstrip()


# 6、拆分和连接
string.partition(str)	有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.
string.rpartition(str)	类似于 partition()函数,不过是从右边开始查找.
*string.split(str="", num=string.count(str))	以str为分隔符切片 string，如果 num有指定值，则仅分隔num个子字符串
string.splitlines([keepends])	按照行('\r','\r\n',\n')分隔，返回一个包含各行作为元素的列表，如果参数keepends为False，不包含换行符，如果为True，则保留换行符。
*string.join(seq)	以string作为分隔符，将seq中所有的元素(的字符串表示)合并为一个新的字符串





string.count(str, beg=0, end=len(string))	返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
bytes.decode(encoding='UTF-8', errors='strict')	Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象
string.encode(encoding='UTF-8', errors='strict')	以 encoding 指定的编码格式编码 string，编码的结果是一个bytes对象。如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
string.expandtabs(tabsize=8)	把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8。
string.format()	格式化字符串
string.maketrans(intab, outtab)	maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
max(str)	返回字符串 str 中最大的字母。
min(str)	返回字符串 str 中最小的字母。
string.translate(str, del="")	根据 str 给出的表(包含 256 个字符)转换 string 的字符,要过滤掉的字符放到 del 参数中
string.zfill(width)	返回长度为 width 的字符串，原字符串 string右对齐，前面填充0






# 字符串的切片

# 切片方法适用于 字符串、列表、元组
	# 切片使用索引值来限定范围，从一个大的字符串中切出小的字符串
	# 列表和元组都是有序的集合，都能够通过索引值获取到对应的数据
	# 字典是一个无序的集合，是使用键值对保存数据


字符串[开始索引:结束索引:步长]

# 字符串逆序
num_str[::-1]
