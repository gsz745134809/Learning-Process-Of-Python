# LeetCode_72.py

# 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

# 你可以对一个单词进行如下三种操作：

# 插入一个字符
# 删除一个字符
# 替换一个字符
# 示例 1:

# 输入: word1 = "horse", word2 = "ros"
# 输出: 3
# 解释: 
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 示例 2:

# 输入: word1 = "intention", word2 = "execution"
# 输出: 5
# 解释: 
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n +1)] for _ in range(m + 1)]
		
		# 初始状态
		for i in range(m+1):
			dp[i][0] = i
		for j in range(n+1):
			dp[0][j] = j

		for i in range(1, m+1):
			for j in range(1, n+1):
				dp[i][j] = min(dp[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1),
								dp[i-1][j] + 1,
								dp[i][j-1] + 1)

		return dp[m][n]     



	def minDistance2(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        result = [{} for _ in range(len(word1) + 1)]

        def getDistance(i, j):
            if i == 0: return j
            if j == 0: return i
            if j in result[i]: return result[i][j]

            if word1[i - 1] == word2[j - 1]:
                distance = getDistance(i - 1, j - 1)
            else:
                distance = min(getDistance(i - 1, j - 1),
                              getDistance(i - 1, j),
                              getDistance(i, j - 1)) + 1
            result[i][j] = distance
            return distance

        return getDistance(len(word1), len(word2))



    def minDistance3(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        d = {}
        def helper(a, b):
            if a * b == 0:
                return a + b
            if (a,b) not in d:
                if word1[a-1] == word2[b-1]:
                    d[a,b] = helper(a-1, b-1)
                else:
                    d[a,b] = 1 + min(helper(a-1, b), helper(a,b-1), helper(a-1,b-1))
            return d[a,b]
        return helper(len(word1), len(word2))
