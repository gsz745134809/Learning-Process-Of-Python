# 搜索二维矩阵II

# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
# 示例:

# 现有矩阵 matrix 如下：

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# 给定 target = 5，返回 true。

# 给定 target = 20，返回 false。



class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:  # 判断是否是[],或者是[[]]
            return False
        
        rows = len(matrix)  # 矩阵行数
        cols = len(matrix[0])  # 矩阵列数
        r = rows - 1  # 行数减一
        c = 0  
        while c < cols and r >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                r -= 1
            else:
                c += 1
        return False









