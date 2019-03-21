# Python 正则表达 RegEx

# 导入模块
import re

# 简单 Python 匹配
# matching string
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print(pattern1 in string)    
print(pattern2 in string)
'''
True
False
'''

# 用正则寻找配对
# regular expression
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print(re.search(pattern1, string))  
print(re.search(pattern2, string))
'''
<_sre.SRE_Match object; span=(12, 15), match='cat'>
None
'''

# 匹配多种可能 使用 []
# multiple patterns ("run" or "ran")
ptn = r"r[au]n"       
print(re.search(ptn, "dog runs to cat"))
'''
<_sre.SRE_Match object; span=(4, 7), match='run'>
'''

# 匹配更多种可能
# continue
print(re.search(r"r[A-Z]n", "dog runs to cat"))     
print(re.search(r"r[a-z]n", "dog runs to cat"))     
print(re.search(r"r[0-9]n", "dog r2ns to cat"))     
print(re.search(r"r[0-9a-z]n", "dog runs to cat"))
'''
None
<_sre.SRE_Match object; span=(4, 7), match='run'>
<_sre.SRE_Match object; span=(4, 7), match='r2n'>
<_sre.SRE_Match object; span=(4, 7), match='run'>
'''

# # 特殊种类匹配

# 数字
# \d : decimal digit
print(re.search(r"r\dn", "run r4n"))                
# \D : any non-decimal digit
print(re.search(r"r\Dn", "run r4n"))
'''
<_sre.SRE_Match object; span=(4, 7), match='r4n'>
<_sre.SRE_Match object; span=(0, 3), match='run'>
'''

# 空白
# \s : any white space [\t\n\r\f\v]
print(re.search(r"r\sn", "r\nn r4n"))               
# \S : opposite to \s, any non-white space
print(re.search(r"r\Sn", "r\nn r4n"))
'''
<_sre.SRE_Match object; span=(0, 3), match='r\nn'>
<_sre.SRE_Match object; span=(4, 7), match='r4n'>
'''

# 所有字母数字和"_"
# \w : [a-zA-Z0-9_]
print(re.search(r"r\wn", "r\nn r4n"))               
# \W : opposite to \w
print(re.search(r"r\Wn", "r\nn r4n"))
'''
<_sre.SRE_Match object; span=(4, 7), match='r4n'>
<_sre.SRE_Match object; span=(0, 3), match='r\nn'>
'''

# 空白字符
# \b : empty string (only at the start or end of the word)
print(re.search(r"\bruns\b", "dog runs to cat"))    
# \B : empty string (but not at the start or end of a word)
print(re.search(r"\B runs \B", "dog   runs  to cat"))
'''
<_sre.SRE_Match object; span=(4, 8), match='runs'>
<_sre.SRE_Match object; span=(5, 11), match=' runs '>
'''

# 特殊字符 任意字符
# \\ : match \
print(re.search(r"runs\\", "runs\ to me"))          
# . : match anything (except \n)
print(re.search(r"r.n", "r[ns to me"))
'''
<_sre.SRE_Match object; span=(0, 5), match='runs\\'>
<_sre.SRE_Match object; span=(0, 3), match='r[n'>
'''

# 句尾句首
# ^ : match line beginning
print(re.search(r"^dog", "dog runs to cat"))        
# $ : match line ending
print(re.search(r"cat$", "dog runs to cat"))
'''
<_sre.SRE_Match object; span=(0, 3), match='dog'>
<_sre.SRE_Match object; span=(12, 15), match='cat'>
'''

# 是否
In [13]:
# ? : may or may not occur
print(re.search(r"Mon(day)?", "Monday"))            
print(re.search(r"Mon(day)?", "Mon"))
'''
<_sre.SRE_Match object; span=(0, 6), match='Monday'>
<_sre.SRE_Match object; span=(0, 3), match='Mon'>
'''

# 多行匹配
# multi-line
string = """
dog runs to cat.
I run to dog.
"""
print(re.search(r"^I", string))                     
print(re.search(r"^I", string, flags=re.M))
None
'''
<_sre.SRE_Match object; span=(18, 19), match='I'>
'''

# 0或多次
# * : occur 0 or more times
print(re.search(r"ab*", "a"))                       
print(re.search(r"ab*", "abbbbb"))
'''
<_sre.SRE_Match object; span=(0, 1), match='a'>
<_sre.SRE_Match object; span=(0, 6), match='abbbbb'>
'''

# 1或多次
# + : occur 1 or more times
print(re.search(r"ab+", "a"))                       
print(re.search(r"ab+", "abbbbb"))
'''
None
<_sre.SRE_Match object; span=(0, 6), match='abbbbb'>
'''

# 可选次数
# {n, m} : occur n to m times
print(re.search(r"ab{2,10}", "a"))                  
print(re.search(r"ab{2,10}", "abbbbb"))
'''
None
<_sre.SRE_Match object; span=(0, 6), match='abbbbb'>
'''

# group 组
# group
match = re.search(r"(\d+), Date: (.+)", "ID: 021523, Date: Feb/12/2017")
print(match.group())                                
print(match.group(1))                               
print(match.group(2))
'''
021523, Date: Feb/12/2017
021523
Feb/12/2017
'''

match = re.search(r"(?P<id>\d+), Date: (?P<date>.+)", "ID: 021523, Date: Feb/12/2017")
print(match.group('id'))                            
print(match.group('date'))
'''
021523
Feb/12/2017
'''

# 寻找所有匹配
# findall
print(re.findall(r"r[ua]n", "run ran ren"))
'''
['run', 'ran']
'''
# | : or
print(re.findall(r"(run|ran)", "run ran ren"))
'''
['run', 'ran']
'''

# 替换
# re.sub() replace
print(re.sub(r"r[au]ns", "catches", "dog runs to cat"))
'''
dog catches to cat
'''

# 分裂
# re.split()
print(re.split(r"[,;\.]", "a;b,c.d;e"))
'''
['a', 'b', 'c', 'd', 'e']
'''

# compile
# compile
compiled_re = re.compile(r"r[ua]n")
print(compiled_re.search("dog ran to cat"))
'''
<_sre.SRE_Match object; span=(4, 7), match='ran'>
'''