def shell_sort(alist):
    n = len(alist)
    # 初始步长
    gap = n / 2
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, n):
            j = i
            # 插入排序
            while j>=gap and alist[j-gap] > alist[j]:
                alist[j-gap], alist[j] = alist[j], alist[j-gap]
                j -= gap
        # 得到新的步长
        gap = gap / 2

alist = [54,26,93,17,77,31,44,55,20]
shell_sort(alist)
print(alist)

"""
最优时间复杂度：根据步长序列的不同而不同
最坏时间复杂度：O(n2)
稳定想：不稳定
"""
