# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

# 说明：本题中，我们将空字符串定义为有效的回文串。

# 示例 1:

# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:

# 输入: "race a car"
# 输出: false


import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W|_', '', s).lower()
        return s[::-1] == s
           


# filter() 函数
# 描述

# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。

# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中。

# 语法

# 以下是 filter() 方法的语法:

# filter(function, iterable)

# 参数

#     function -- 判断函数。
#     iterable -- 可迭代对象。

# 返回值

# 返回一个迭代器对象



# join() 方法
# 描述

# Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
# 语法

# join()方法语法：

# str.join(sequence)

# 参数

#     sequence -- 要连接的元素序列。

# 返回值

# 返回通过指定字符连接序列中元素后生成的新字符串。


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(filter(str.isalnum,s)).lower()
        return s==s[::-1]


# 逐个字符判断
class Solution:
    def isPalindrome(self, s: 'str') -> 'bool':
        s = [c for c in s if c .isalpha() or c.isdigit()]
        if len(s) <= 1:
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1
        return True
