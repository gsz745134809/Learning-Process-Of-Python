# 简单表节点类
class LNode(object):
    def __init__(self, val, next_=None):
        self.val = val  # 节点值
        self.next = next_  # 指向下一个节点

head = LNode(0)  # 创建头节点

# 表首端插入
# 1、创建一个新节点并存入数据，即下面的q
# 2、把原链表（即head）首节点的链接存入新节点的链接域next，这一操作将原表的一串节点链接在刚创建的新节点之后
# 3、修改表头变量，使之指向新节点，这个操作使新节点实际成为表头变量所指的节点，即表的首节点，q的值成为这个表的首元素
q = LNode(12)  # 创建一个新链表节点，节点值为12
q.next = head.next  # 把原链表的首节点的链接存入新节点的链接域next
head = q  # 修改表头变量，使之指向新的节点

# print(q.val, head.val)
# 12 12



# 一般情况的元素插入
# 1、创建一个新节点并存入数据
# 2、把pre所指节点next域的值存入新节点的链接域next，这个操作将原表在pre所指节点之后的一段链接到新的节点之后。
# 3、修改pre的next域，使之指向新节点，这个操作把新节点链入被操作的表。
pre = LNode(1)
last = LNode(3)
pre.next = last  # 原来的链表为 1 -> 3

q = LNode(2)
q.next = pre.next
pre.next = q
while pre:
    # print(pre.val)
    pre = pre.next
# 1 2 3


# 删除元素

# 删除表首元素
head = head.next

# 一般元素的删除
pre.next = pre.next.next



# 扫描、定位和遍历
'''
每个扫描循环必须用一个扫描指针作为控制变量，每步迭代前必须检查其值是否为None，保证随后操作的合法性。
'''
p = head  # 辅助变量 p 称为扫描指针
while p is not None:
    # processing
    p = p.next


# 按下标定位：
# 给定 i ，确定第 i 个元素所在节点的操作称为按下标定位。
p = head
while p is not None and i > 0:
    i -= 1
    p = p.next


# 按元素定位：假设需要在链表里找到满足谓词pred的元素。
p = head
while p is not None and not pred(p.val):
    p = p.next




# 求表的长度
# O(n)
def length(head):
    p, n = head, 0
    while p is not None:
        n += 1
        p = p.next
    return n
'''
利用表头记录表长度
'''





# 单链表类的实现

llist1 = LNode(1)
p = llist1  # 利用p作为头节点

for i in range(2, 11):
    p.next = LNode(i)
    p = p.next

p = llist1
while p is not None:
    print(p.val)
    p = p.next





# 输出表
# 放在创建链表类里面
def printall(self):
    p = self.head
    while p is not None:
        print(p.val, end='')
        if p.next is not None:
            print(', ', end='')
        p = p.next
    print('')






# 在单链表对象增加一个尾节点引用域
# 可以采用头节点不存储数据，而是存储下一个节点的引用和尾节点的引用





# 循环单链表（简称循环链表），其最后一个节点的next域不用None，而是指向表的第一个节点
#

class LCList:  # 循环单链表类
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):  # 前端插入
        p = LNode(elem)
        if self._rear is None:
            p.next = p  # 建立一个节点的环
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear = self._rear.next

    def append(self, elem):  # 尾端插入
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):  # 前端弹出
        if self._rear is None:
            raise LinkedListUnderflow("in pop of CLList")
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def printall(self):  # 输出表元素
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next





# 双链表

# 节点操作
p.next.next = p.next
p.next.prev = p.prev

# 双链表类
class DLnode(LNode):
    def __init__(self, val, prev=None, next_=None):
        LNode.__init__(self, val, next_)
        self.prev = prev
