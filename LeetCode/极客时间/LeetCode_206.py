# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def reverseList(head):
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
        # 以上等价与
        # r = cur.next
        # cur.next = prev
        # prev = cur
        # cur = r
    return prev
