# DP

"""

sums记录子序和

max_sum记录最大子序和

遍历nums，如果当前子序和大于0，则加到当前子序和sums中，
        如果当前子序和小于或等于0，则将temp的值赋给sums作为当前的新开始

最后将当前最大子序和max_sum和当前子序和sums相比较，得到较大的一个，赋值给当前最大子序和max_sum

"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = 0
        max_sum = nums[0]
        for temp in nums:
            if sums > 0:
                sums += temp
            else:
                sums = temp
            max_sum = max(max_sum, sums)
        return max_sum



# 时间最少

class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        if len(nums) == 1:
            return nums[0]
        
        cur_max = end_max = nums[0]
        for i in range(1, len(nums)):        
            end_max = end_max + nums[i] if end_max > 0 else nums[i]
            cur_max = max(end_max, cur_max)
        return cur_max
