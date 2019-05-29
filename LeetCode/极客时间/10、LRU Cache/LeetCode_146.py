# LeetCode_146.py

# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。
# 当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

# 进阶:

# 你是否可以在 O(1) 时间复杂度内完成这两种操作？

# 示例:

# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4



class LRUCache:

    def __init__(self, capacity: int):
    	self.dic = collections.OrderedDict()
    	self.remain = capacity
        
    def get(self, key: int) -> int:
    	if key not in self.dic:
    		return -1
    	v = self.dic.pop(key)
    	self.dic[key] = v  # set key as the newest one
    	return v        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
        	self.dic.pop(key)
        else:
        	if self.remain > 0:
        		self.remain -= 1
        	else:  # self.dic is full
        		self.dic.popitem(last=False)
        self.dic[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)







from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.dic=OrderedDict()       

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            val=self.dic[key]
            del self.dic[key]
            self.dic[key]=val
            return val
        else:
            return -1        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic:
            del self.dic[key]
        elif len(self.dic)==self.capacity:
            self.dic.popitem(False)
        self.dic[key]=value
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)