'''
动态规划 （Dynamic Programming）

1、 递归 + 记忆化 -->  递推  （从下到上）

2、 状态的定义： opt[n], dp[n], fib[n]

3、 状态转移方程：
		opt[n] = best_of(opt[n-1], opt[n-2], ...)

4、 最优子结构
'''





'''
DP  VS  回溯  VS  贪心

· 回溯（递归） ---- 重复计算
· 贪心 ---- 永远局部最优
· DP ---- 记录局部最优子结构/多种记录值

'''



# DP代码模板

# 状态定义
dp = new int [m + 1][n + 1]

# 初始状态
dp[0][0] = x
dp[0][1] = y
...

# DP状态的推导
for i in range(n):
	for j in range(m):
		...
		dp[i][j] = min{dp[i-1][j], dp[i][j-1], etc.}

return dp[m][n]  # 最优解

