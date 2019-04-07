# LeetCode_200.py

# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

# 示例 1:

# 输入:
# 11110
# 11010
# 11000
# 00000

# 输出: 1
# 示例 2:

# 输入:
# 11000
# 11000
# 00100
# 00011

# 输出: 3



'''
未完成
'''




import collections

class Solution:

	self.dx = [-1, 1, 0, 0]
	self.dy = [0, 0, -1, 1]

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
        	return 0
        self.max_x = len(grid)
        self.max_y = len(grid[0])
        self.grid = grid
        return sum([self.floodfill_DFS(i, j) for i in range(self.max_x) for j in range(self.max_y)])

    def floodfill_DFS(self, x, y):
    	if not self._is_valid(x, y):
    		return 0
    	self.visited.add((x, y))
    	for k in range(4):
    		self.floodfill_DFS(x + dx[k], y + dy[k])
    	return 1

    def _is_valid(self, x, y):
    	if x < 0 or x >= self.max_x or y < 0 or y >= self.max_x:
    		return False
    	if self.grid[x][y] == '0' or ((x, y) in self.visited):
    		return False
    	return True


    def floodfill_BFS(self, x, y):
    	if not self._is_valid(x, y):
    		return

    	self.visited.add((x, y))
    	queue = collections.deque()
    	queue.append((x, y))

    	while queue:
    		cur_x, cur_y = queue.popleft()
    		for i in range(4):
    			new_x, new_y = cur_x + dx[i], cur_y + dy[i]
    			if self._is_valid(new_x, new_y):
    				self.visited.add((new_x, new_y))
    				queue.append((new_x, new_y))


#TODO unfinished
class Solution(object):
	def numIslands(self, grid):
		if not grid or not grid[0]:
			return 0

		uf = UnionFind(grid)
		directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
		m, n = len(grid), len(grid[0])

		for i in range(m): 
			for j in range(n):
				if grid[i][j] == '0':
					continue
			for d in directions:
				nr, nc = i + d[0], j + d[1]
				if nr >= 0 and nc >= 0 and nr < m and nc < n and grid[nr][nc] == '1':
					uf.union(i*n+j, nr*n+nc)

		return uf.count



# 并查集
class UnionFind(object):
	def __init__(self, grid):
		m, n = len(grid), len(grid[0])
		self.count = 0
		self.parent = [-1] * (m*n)
		self.rank = [0] * (m*n)
		for i in range(m):
			for j in range(n):
				if grid[i][j] == '1':
					self.parent[i*n + j] = i*n + j  # 二维转一维
					self.count += 1

	def find(self, i):
		if self.parent[i] != i:
			self.parent[i] = self.find(self.parent[i])
		return self.parent[i]

	def union(self, x, y):
		rootx = self.find(x)
		rooty = self.find(y)
		if rootx != rooty:
			if self.rank[rootx] > self.rank[rooty]:
				self.parent[rooty] = rootx
			elif self.rank[rootx] < self.rank[rooty]:
				self.parent[rootx] = rooty
			else:
				self.parent[rooty] = rootx
				self.rank[rootx] += 1
			self.count -= 1

