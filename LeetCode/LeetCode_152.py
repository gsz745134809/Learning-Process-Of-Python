# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

# 示例 1:

# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 示例 2:

# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。



class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums is None:
        	return 0

        dp = [[0 for _ in range(2)] for _ in range(2)]  # 两行两列的列表

        dp[0][1], dp[0][0], res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):  # 遍历nums
        	x, y = i % 2, (i-1) % 2  # 010101，滚动数组
        	dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])  # 对于最大值
        	dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])  # 对于负的最大值
        	res = max(res, dp[x][0])

        return res





    def maxProduct1(self, nums):
    	if nums is None:
    		return 0

    	res, curMax, curMin = nums[0], nums[0], nums[0]

    	for i in range(1,len(nums)):
    		num = nums[i]
    		curMax, curMin = curMax * num, curMin * num
    		curMin, curMax = min(curMax, curMin, num), max(curMax, curMin, num)
    		# print(curMin, curMax)
    		res = curMax if curMax > res else res
    	return res

	def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A = nums
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(max(A),max(B)) 