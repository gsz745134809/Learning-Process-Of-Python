# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 删除链表中的重复元素

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        if head.next is None:
            return head
        ans = head
        while 1:
            if head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
            if head.next is None:
                return ans
