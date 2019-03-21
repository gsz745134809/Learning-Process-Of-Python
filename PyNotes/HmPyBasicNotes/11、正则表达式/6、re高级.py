# re模块的高级用法

# search
# 匹配处文章阅读的次数
import re
ret = re.search(r"\d+", "阅读次数为 9999，点赞次数为100")
ret.group()
# 不用从头开始匹配，按照正则匹配第一个数
[out]: '9999'



# findall
统计处python、c、c++相应文章阅读的次数
ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
# 返回一个列表
print(ret)
[out]: ['9999', '7890', '12345']



# sub 
# 将匹配到的数据进行替换
将匹配到的阅读次数加1

#Method one:
import re
ret = re.sub(r"\d+", '998', "python = 997, c++ = 1024")
print(ret)

[out]: 'python = 998, c++ = 998'


#Method two:
import re
def add(temp):
	strNum = temp.group()
	num = int(strNum) + 1
	return str(num)
	
ret = re.sub(r'\d+', add, 'python = 997')
print(ret)

[out]: 'python = 998'











# split
# 根据匹配进行切割字符串

切割字符串"info:xiaoZhang 33 shandong"
import re
ret = re.split(r":| ", "info:xiaoZhang 33 shandong")
print(ret)

[out]: ['info', 'xiaoZhang', '33', 'shandong']



















































