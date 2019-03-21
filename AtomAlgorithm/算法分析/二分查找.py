
# 二分查找

def BinarySearch(arr, x):
    Low = 0
    High = len(arr)-1
    while High >= Low:
        Mid = (Low+High)//2
        if arr[Mid] < x:
            Low = Mid + 1
        elif arr[Mid] > x:
            High = Mid - 1
        else:
            return Mid
    return -1


arr = [2, 5, 9, 11]
print(BinarySearch(arr, 5))


# O(logn)
