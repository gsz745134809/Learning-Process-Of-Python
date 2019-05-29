# 二分查找 Binary Search
# 1、Sorted
# 2、Bounded
# 3、Accessible by index


left, right = 0, len(array) - 1
while left <= right:
    mid = left + (right - left) / 2
    if array[mid] == target:
        # find the target!
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
