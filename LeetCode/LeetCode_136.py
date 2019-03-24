nums = [2,2,1]


# 高级用法异或^
# 0异或任何数不变，任何数与自己异或为0。a⊕b⊕a=b。
# 异或满足加法结合律和交换律。
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res^=i
        return res

print(singleNumber(nums))



# s = []
# for i in nums:
# 	if i not in s:
# 		s.append(i)
# 	elif i in s:
# 		s.remove(i)
# # return s[0]
# print(s[0])




# return sum(set(nums))*2-sum(nums)
