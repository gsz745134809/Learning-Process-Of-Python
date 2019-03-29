# LeetCode_120.py

# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

# 例如，给定三角形：

# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

# 说明：

# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。


class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle == []:
            return 0
        for i in range(len(triangle)-1, 0, -1):
            for j in range(len(triangle[i])-1):
                triangle[i-1][j] += min(triangle[i][j], triangle[i][j+1])
        return triangle[0][0]

    def minimumTotal2(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        k = len(triangle)
        if k == 0:
            return 0
        elif k == 1:
            return triangle[0][0]
        else:
            for m in range(k-2,-1,-1):
                for n in range(0,m+1):
                    if triangle[m+1][n] < triangle[m+1][n+1]:
                        triangle[m][n] = triangle[m][n] + triangle[m+1][n]
                    else:
                        triangle[m][n] = triangle[m][n] + triangle[m+1][n+1]
        
        return triangle[0][0]


 #    def minnimumTotal3(self, triangle: List[List[int]]) -> int:  
 #        i = len(triangle)  # 行数
 #        j = len(triangle[-1])  # 列数
 #        dp = [[0 for _ in range(j)] for _ in range(i)]
 #        for m in range(j):
 #            dp[i-1][m] = triangle[i-1][m]
        
 #        while i-2>=0:  
 #            j = i
 #            while j-2>=0:
 #                dp[i-2][j-2] = min(dp[i-1][j-2],dp[i-1][j-1]) + triangle[i-2][j-2]
 #                j -= 1
 #            i -= 1
            
 #        return dp[0][0]