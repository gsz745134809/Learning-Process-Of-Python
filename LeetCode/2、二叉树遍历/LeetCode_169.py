
def majorityElement(nums):
    dict1 = {}
    for i in nums:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] +=1
    return max(dict1,key=dict1.get)

nums = [1,2,3,3,3]
print(majorityElement(nums))




class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = int(len(nums)/2)
        return nums[n]