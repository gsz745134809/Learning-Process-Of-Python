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

# 双链表节点
class DLNode(LNode):
    def __init__(self, val, prev=None, next_=None):
        LNode.__init__(self, val, next_)
        self.prev = prev



# 双链表类
class DLList(LList1):
    # 双链表类
    def __init__(self):
        LList1.__init__(self)

    def prepend(self, val):
        p = DLNode(val, None, self._head)
        if self._head is None:  # 空表
            self._rear = p
        else:  # 非空表，设置next引用
            p.next.prev = p
        self._head = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop of DLList")
        e = self._head.val
        self._head = self._head.next
        if self._head is not None:  # _head空时不需要做任何事
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last of DLList")
        e = self._rear.val
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None  # 设置 _head 保证 is_empty 正确工作
        else:
            self._rear.next = None
        return e





# 单链表反转
# 从一个表的首端不断取下结点，将其加入另一个表的首端，就形成了一个反转的过程
# 取下和加入操作都是O(1)
# 总：O(n)

def rev(head):  # 传入的参数为一个链表的表头的引用
    prev = None
    while head is not None:  # 遍历链表
        cur = head  # 实际用q， head指向表头
        head = cur.next  # 摘下原来的首结点
        cur.next = prev
        prev = cur  # 将刚摘下的结点加入p引用的结点序列
    head = prev  # 反转后的结点序列已经做好，重置表头链接

def reverseList(head):
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

# 参考：https://blog.csdn.net/weixin_39561100/article/details/79818949





# 单链表排序

# 先看列表的插入排序
def list_sort(lst):
	for i in range(1, len(lst)):  # 开始时片段[0:1]已经排序
		x = lst[i]
		j = i
		while j > 0 and lst[j-1] > x:
			lst[j] = lst[j-1]
			j -= 1
		lst[j] = x


# 单链表的排序
# 扫描指针 crt 指向当前考虑的结点，对一个大循环中每次处理一个表元素并前进一步
# 对每个元素的处理分两步完成：
# 第一步从头开始扫过小于或等于x的表元素，直至确定了已排序段里的特定位置，找到了第一个大于x的表元素
# 第二步是做一系列“倒换”，把x放入正确位置，并将其他表元素后移。
def sort1(self):
	if self._head is None:
		return
	crt = self._head.next  # 从首结点之后开始处理
	while crt is not None:
		x = crt.val
		p = self._head
		while p is not crt and p.val <= x:  # 跳过最小元素
			p = p.next
		while p is not crt:  # 倒换大元素，完成元素插入的工作
			y = p.val
			p.val = x
			x = y
			p = p.next
		crt.val = x  # 回填最后一个元素
		crt = crt.next


def sort(self):
	p = self._head
	if p is None or p.next is None:
		return

	rem = p.next
	p.next = None
	while rem is not None:
		p = self._head
		q = None
		while p is not None and p.val <= rem.val:
			q = p
			p = p.next
		if q is None:
			self._head = rem
		else:
			q.next = rem
		q = rem
		rem = rem.next
		q.next = p
		




































