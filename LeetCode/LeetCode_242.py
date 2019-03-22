# def isAnagram(s, t):
#     lis = [i for i in s]
#     lis.sort()
#     lit = [i for i in t]
#     lit.sort()
#     if lis == lit:
#         return True
#     else:
#         return False
#
# s = "a"
# t = "aba"
# print(isAnagram(s, t))



# Map :计数
# {letter : count}

def isAnagram1(s, t):
    dic1, dic2 = {}, {}
    for item in s:
        dic1[item] = dic1.get(item, 0) + 1
    for item in t:
        dic2[item] = dic2.get(item, 0) + 1
    return dic1 == dic2




# 此处自己构造了一个hashmap（本题中全是小写字母）
def isAnagram2(s, t):
    dic1, dic2 = [0]*26, [0]*26  # 创建一个含有二十六个元素的列表
    for item in s:
        dic1[ord(item)-ord('a')] += 1
    for item in t:
        dic2[ord(item)-ord('a')] += 1
    return dic1 == dic2
