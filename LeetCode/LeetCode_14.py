"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

"""


"""

之前有一个类似的题，求两个字符串的最大公共前缀，有一种思想是将两个字符串放在二维数组对应位置，
相同填1，不同填0，最终看对角线（位置(i,i)上）上1的个数

"""

# 粗制滥造写法:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        _null = ""
        if len(strs) == 0:
            return _null
        i = 0
        while i <= len(strs[0]) :   
            flag = strs[0][:i]
            for item in strs:
                if len(item) < i:
                    return strs[1][:i-1]
                if flag == item[:i]:
                    continue
                else :
                    return strs[1][:i-1]
            i += 1
        return strs[0][:i-1]







# 时间最少解法
class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if not strs:
            return''
        if len(strs)==1:
            return strs[0]
        strs.sort()
        p=''
        for x,y in zip(strs[0],strs[-1]):
            if x==y:
                p+=x
            else:
                break
        return p






