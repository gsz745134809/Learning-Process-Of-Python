"""

给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""





'''

遍历字符串，如果遇到相同元素的则返回第一次发现该元素位置处重新开始遍历。
每次遍历得到当前子串就改变相应原始字符串。

'''



# 菜鸡解法：
def lengthOfLongestSubstring(s):
    cur_str = ""
    flag_str = ""
    i = 0
    while i < len(s):
        if s[i] not in cur_str:
            cur_str += s[i]
            i += 1
            # print('cur_per', cur_str)
            # print(s)
        else:
            if len(flag_str) < len(cur_str):
                flag_str = cur_str
                cur_str = ""
                s = s[s.find(s[i]) + 1:]
                i = 0
            else:
                cur_str = ""
                s = s[s.find(s[i]) + 1:]
                i = 0

    # print('cur', cur_str)
    # print('flag', flag_str)
    return max(len(flag_str), len(cur_str))


# s = "jbpnbwwd"

# print(lengthOfLongestSubstring(s))




# 用时最少解法：
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s=='':   #01.特殊情况
            return 0
        
        small=''   #02.初始赋值
        tem_len=1
        
        for i in s:   
            if (i in small): #03.如果有重复，在最后一位的，字符变成最后一位；在j位的，字符变成j+1：+j。
                if i != small[-1]:
                    j=small.index(i)
                    small=small[j+1:]+i
                else:
                    small=i

            else:        #04.无重复才可能长度增加
                small+=i
                if len(small) > tem_len:
                    tem_len=len(small)
        print(small)
        return tem_len



# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
        
#         if s=='':
#             return 0
#         small=''
#         tem_len=1
        
#         for i in s:
#             if (i in small):
#                 if i == small[-1]:
#                     small=i
#                 else:
#                     j=small.index(i)
#                     small=small[j+1:]+i
#             else:
#                 small+=i
#                 if len(small) > tem_len:
#                     tem_len=len(small)
#         print(small)
#         return tem_len
                    