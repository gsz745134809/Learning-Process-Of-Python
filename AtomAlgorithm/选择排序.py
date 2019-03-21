# def findSmallest(arr):
#     smallest = arr[0]  # 存储最小的值
#     smallest_index = 0  # 存储最小元素的索引
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index
#
#
# def selectionSort(arr):
#     """对数组进行排序"""
#     newArr = []
#     for i in range(len(arr)):
#         smallest = findSmallest(arr)  # 找出数组中最小的元素，并将其加入到新数组中
#         newArr.append(arr.pop(smallest))
#     return newArr
#
# arr = [5, 3, 6, 2, 10]
# print(selectionSort(arr))

def selectionSort(arr):

    for j in range(len(arr)):
        smallest = arr[j]  # 假定当前元素为最小
        for i in range(j, len(arr)):
            # 寻找最小元素，并记录该元素的索引
            if arr[i] < smallest:
                smallest = arr[i]
                index = i

        if smallest < arr[j]:
            # 如果当前元素不是最小，则和最小元素交换
            arr[index], arr[j] = arr[j], arr[index]
    return arr

arr = [5, 3, 6, 2, 10, 5, 10, 6]
print(selectionSort(arr))
