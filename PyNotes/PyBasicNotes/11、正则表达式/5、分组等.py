# 匹配分组


|          匹配左右任意一个表达式
(ab)       将括号中字符作为一个分组
\num       引用分组num匹配到的字符串
(?P<name>) 分组起别名
(?P=name)  引用别名为name分组匹配到的字符串



import re

re.match(r"[a-zA-Z0-9_]{4,20}@(163|126)\.com$", "laowang@163.com")

上面代表匹配以 字母数字下划线开头（4到20位）@163.com或者@126.com结尾的字符串





re.match(r"([a-zA-Z0-9_]{4,20})@(163|126)\.com$", "laowang@163.com").group(1)

[out]: laowang





re.match(r"<(?P<p1>\w*)>.*</(?P=p1)>", "<h1>hahaha</h1>").group()
            (?P<p1>\w*)     (?P=p1)
               分组         匹配分组
此处代表匹配前后尖括号里面的内容一致




# 取别名
re.match(r"<(\w*)>.*</\1>", "<h1>hahaha</h1>").group()

























