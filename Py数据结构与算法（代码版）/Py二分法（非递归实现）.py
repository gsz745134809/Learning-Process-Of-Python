def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    while first <= last:
        midpoint = (first + last) // 2
        # TODO(郭) 验证分割线位置
        if alist[midpoint] == item:
            return True
        elif item < alist[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return False


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))
