# 利用排序
import bisect
class KthLargest:
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = sorted(nums)
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        bisect.insort_left(self.nums, val)
        return self.nums[-self.k]

# 利用最小堆
import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val):
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]
# 时间最少





















class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pool = nums
        self.size = len(self.pool)
        self.k = k
        #heapq.heapify()将列表原地转换为堆并排序
        heapq.heapify(self.pool)
        while self.size > k:
            heapq.heappop(self.pool)
            self.size -= 1

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.size < self.k:
            heapq.heappush(self.pool, val)
            self.size += 1
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)




# 说明
'''
本模块实现了堆队列算法，也叫作优先级队列算法。堆队列是一棵二叉树，并且拥有这样特点，它的父节点的值小于等于任何它的子节点的值，如果采用数组array实现，可以把它们的关系表示为：heap[k] <= heap[2*k+1] 和 heap[k] <= heap[2*k+2]，对于所有k值都成立，k值从0开始计算。作为比较，可以认为不存的元素是无穷大的。堆队列有一个比较重要的特性，它的最小值的元素就是在根：heap[0]。 下面的API与教科书上堆算法有两点差别：(a)使用0开始的索引。这样可能会让大家看到节点层次的索引上有点别扭的，但这样更适合python语言处理，因为python是以0为开始计算数组和列表的索引。(b)弹出的方法返回的值是最小值，而不是最大值（在教科书上叫作最小堆，最大堆在教科书更通用地使用来教学，因为它更适合排序算法）。基于上面两点可以查看一个堆：heap[0]返回一个最小值的项，heap.sort()对整个堆进行排序。
#创建一个堆队列，可以使用一个列表[]，也可以使用heapify(x)函数。
#heapq.heappush(heap, item)
#把一项值压入堆heap，同时维持堆的排序要求。
'''
#例子：
#python 3.4
import heapq
h = []
heapq.heappush(h, 5)
heapq.heappush(h, 2)
heapq.heappush(h, 8)
heapq.heappush(h, 4)
print(heapq.heappop(h))
#结果输出如下：
2
--------------------------------------------------------------------------------
#heapq.heappop(heap)
#弹出并返回堆里最小值的项，调整堆排序。如果堆为空，抛出异常IndexError。
#例子：
#python 3.4
import heapq
h = []
heapq.heappush(h, 5)
heapq.heappush(h, 2)
heapq.heappush(h, 8)
heapq.heappush(h, 4)
print(heapq.heappop(h))
print(heapq.heappop(h))
#结果输出如下：
2

4
--------------------------------------------------------------------------------------
#heapq.heappushpop(heap, item)
#向堆里插入一项，并返回最小值的项。组合了前面两个函数，这样更加有效率。
#例子：
#python 3.4
import heapq
h = []
heapq.heappush(h, 5)
heapq.heappush(h, 2)
heapq.heappush(h, 8)
print(heapq.heappushpop(h, 4))
#结果输出如下：
2
--------------------------------------------------------------------------------------
#heapq.heapify(x)
#就地转换一个列表为堆排序，时间为线性。
#例子：
#python 3.4
import heapq
h = [9, 8, 7, 6, 2, 4, 5]
heapq.heapify(h)
print(h)
#结果输出如下：
[2, 6, 4, 9, 8, 7, 5]
------------------------------------------------------------------------------------
#heapq.heapreplace(heap, item)
#弹出最小值的项，并返回相应的值，最后把新项压入堆。如果堆为空抛出异常IndexError。
#例子：
#python 3.4
import heapq
h = [9, 8, 7, 6, 2, 4, 5]
heapq.heapify(h)
print(h)
print(heapq.heapreplace(h, 1))
print(h)
#结果输出如下：
[2, 6, 4, 9, 8, 7, 5]
2
[1, 6, 4, 9, 8, 7, 5]
-------------------------------------------------------------------------------------
#heapq.merge(*iterables)
#合并多个堆排序后的列表，返回一个迭代器访问所有值。
#例子：
#python 3.4
import heapq
h = [9, 8, 7, 6, 2, 4, 5]
heapq.heapify(h)
l = [19, 11, 3, 15, 16]
heapq.heapify(l)
for i in heapq.merge(h,l):
    print(i, end = ',')
#结果输出如下：
2,3,6,4,9,8,7,5,11,19,15,16,
---------------------------------------------------------------------------------------
#heapq.nlargest(n, iterable, key=None)
#从数据集iterable里获取n项最大值，以列表方式返回。如果参数 key提供，key是一个比较函数，用来比较元素之间的值。
#例子：
#python 3.4
import heapq
h = [9, 1, 7, 6, 2, 4, 5]
l = heapq.nlargest(3, h)
print(l)
#结果输出如下：
[9, 7, 6]
---------------------------------------------------------------------------------------
#heapq.nsmallest(n, iterable, key=None)
#从数据集iterable里获取n项最小值，以列表方式返回。如果参数 key提供，key是一个比较函数，用来比较元素之间的值。相当于：sorted(iterable, key=key)[:n]
#例子：
#python 3.4
import heapq
h = [9, 1, 7, 6, 2, 4, 5]
l = heapq.nsmallest(3, h)
print(l)
#结果输出如下：
[1, 2, 4]
#在最后这两个函数中，如果数量比较少时使用起来比较高效，如果数据量比较大，要使用sorted()函数，如果n=1最好使用内置函数min()或max()。
---------------------------------------------------------------------------------------
#采用堆算法来实现排序：
#例子：
#python 3.4
import heapq
def heapsort(iterable):
    '实现与sorted(iterable)相同的功能'
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

#结果输出如下：

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
