

# 官方题解
# 方法：双指针法
# 算法

# 数组完成排序后，我们可以放置两个指针 i 和 j，其中 i 是慢指针，而 j 是快指针。只要 nums[i] = nums[j]，我们就增加 j 以跳过重复项。

# 当我们遇到 nums[j] =nums[i] 时，跳过重复项的运行已经结束，因此我们必须把它（nums[j]）的值复制到 nums[i+1]。
# 然后递增 i，接着我们将再次重复相同的过程，直到 j 到达数组的末尾为止。

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


# 利用 Python 中的 set ，先去重， 然后排序， 返回列表长度

class Solution:
    def removeDuplicates(self, nums):
        temp = set(nums)
        nums[:] = sorted(list(temp))  # 需要原地修改数组
        return len(set(nums))
