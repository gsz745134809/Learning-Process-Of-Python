def quicksort(array):
    # 平均 O(nlogn)
    # 最坏 O(n^2)
    if len(array) < 2:
        return array  # 基线条件：为空或者只包含一个元素的数组是“有序”的
    else:
        pivot = array[0]  # 递归条件
        less = [i for i in array[1:] if i <= pivot]  # 由所有小于等于基准值的元素组成的子数组

        greater = [i for i in array[1:] if i > pivot]  # 由所有大于基准值的元素组成的子数组

        return quicksort(less) + [pivot] + quicksort(greater)


array = [10, 5, 2, 3]
print(quicksort(array))
