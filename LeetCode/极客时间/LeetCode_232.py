'''
利用两个栈，称为输入栈和输出栈

首先如果要入栈，push到输入栈

每次如果要调用pop或者peek，都要先判断输出栈内是否有元素，
如果输出栈内有元素，先将输出栈内元素pop，
如果输出栈内没有元素，则把输入栈内所有内容先全部pop到输出栈，然后再进行pop或者peek操作
'''


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.item = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.item.insert(0,x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.item.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.item[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.item == []:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
