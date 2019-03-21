def findContentChildren(g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        child = 0
        cookie = 0
        g.sort()  # 先将饼干 和 孩子所需大小都进行排序 （从小到大排序）
        s.sort()
        while (child<len(g) and cookie<len(s)):  # 当其中一个遍历就结束
            if g[child] <= s[cookie]:  # 当用当前饼干可以满足当前孩子的需求，可以满足的孩子数量+1
                child += 1
            cookie += 1  # 饼干只可以用一次，因为饼干如果小的话，就是无法满足被抛弃，满足的话就是被用了
        return child
