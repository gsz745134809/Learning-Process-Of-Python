# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head  # 采用快慢两指针
        while slow and fast and fast.next:
            # 没遍历完
            slow = slow.next
            fast = fast.next.next
            # 快的每次走两步，慢的每次走一步
            if slow is fast:
                # 如果两个相遇
                return True
        return False