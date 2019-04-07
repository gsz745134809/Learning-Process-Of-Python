class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# 或者
# class Solution:
#     def maxDepth(self, root):
#         return root == null ? 0
#         : 1 + Math.max(maxDepth(root.left), maxDepth(root.right))
