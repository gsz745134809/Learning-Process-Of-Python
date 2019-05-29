
class Solution(object):
    def generateParenthesis(self, n):
        self.list = []
        self._gen(0, 0, n, "")
        return self.list

    def _gen(self, left, right, n, result):
        # left 和 right代表左括号和右括号分别已经用了多少个
        if left == n and right == n:
            self.list.append(result)
            return
        if left < n:
            self._gen(left + 1, right, n, result + "(")
        if left > right and right < n:
            self._gen(left, right + 1, n, result + ")")



# 用时最少
class Solution:
    def generate(self, n, l, r):
        if n == l:
            return [')' * (n - r)]
        if l == r:
            return ['(' + i for i in self.generate(n, l + 1, r)]
        else:
            return ['(' + i for i in self.generate(n, l + 1, r)] + [')' + i for i in self.generate(n, l, r + 1)]

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.generate(n, 0, 0)


# 
class Solution:
    def __init__(self):
        self.dp = dict(zip((0, 1), ([''], ['()'])))

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        if n not in self.dp:
            self.dp[n] = ['(' + sl + ')' + sr for m in range(n) for sl in self.generateParenthesis(m) for sr in self.generateParenthesis((n - 1) - m)]

        return self.dp[n]
