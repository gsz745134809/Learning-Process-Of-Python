# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy  # 快指针
        slow = dummy  # 慢指针
        for i in range(n):
            fast = fast.next  # 快指针先走n步
        
        while fast.next != None:  # 直到快指针到达链表最后一个结点
            fast = fast.next    
            slow = slow.next
            
        slow.next = slow.next.next  # 此时慢指针指向倒数第n个结点
        return dummy.next


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = head
        node.prev = None
        # if not head.next and n == 1:
        #     return []
        while node.next:
            temp = node
            node = node.next
            node.prev = temp
        for i in range(n - 1):
            node = node.prev
        if node.prev:
            node.prev.next = node.next
        else:
            head = node.next
        return head


# 1->2->3->4->5
l1 = ListNode(1); l2 = ListNode(2); l3 = ListNode(3); l4 = ListNode(4); l5 = ListNode(5)

l1.next = l2; l2.next = l3; l3.next = l4; l4.next = l5
p = l1
# while p:
# 	print(p.val)
# 	p = p.next














