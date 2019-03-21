# re 模块操作

# 1、re 模块的使用过程

import re  # 导入re模块

result = re.match(正则表达式, 要匹配的字符串)  # 使用match方法进行匹配操作

result.group()  # 如果上一步匹配到数据的话，可以使用group方法来提取数据


# 2、re模块示例（匹配以itcast开头的语句）

import re

result = re.match("itcast", "itcast.cn")

result.group()

[out]: itcast


 





















