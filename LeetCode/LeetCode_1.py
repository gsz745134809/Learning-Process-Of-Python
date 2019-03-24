# 使用set： x+y= 9 => y = 9-x
# For: x: 0-->length
# set : 9-x
# 在Python中表现为字典类型

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #用len()方法取得nums列表长度
        n = len(nums)
        #创建一个空字典
        d = {}
        for x in range(n):
            a = target - nums[x]
            #字典d中存在nums[x]时
            if nums[x] in d:
                return d[nums[x]],x
            #否则往字典增加键/值对
            else:
                d[a] = x
        #边往字典增加键/值对，边与nums[x]进行对比



class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            # 如果找到则返回，没找到就将当前元素增加到字典中
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None
