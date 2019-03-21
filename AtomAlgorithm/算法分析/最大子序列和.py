
def MaxSubsequenSum(arr):
    MaxSum = 0  # initialize最大和
    for i in range(len(arr)):  # 遍历列表
        for j in range(i, len(arr)):  # 遍历从第i个元素开始的片
            ThisSum = 0
            for k in range(i, j+1):  # 在i到j之间寻找最大子序列的和
                ThisSum += arr[k]  # 此处耗时太多，改进如下
                if ThisSum > MaxSum:
                    MaxSum = ThisSum
    return MaxSum

arr = [-2, 11, -4, 13, -5, -2]
print(MaxSubsequenSum(arr))

# time : ∑(i=0~N-1)∑(j=i~N-1)∑(k=i~j)1



# 上面的改进
def MaxSubsequenSum2(arr):
    MaxSum = 0
    for i in range(len(arr)):
        ThisSum = 0
        for j in range(i, len(arr)):
            ThisSum += arr[j]

            if ThisSum > MaxSum:
                MaxSum = ThisSum
    return MaxSum




# 利用递归
def MaxSubSum(arr, left, right):
    if left == right:
        if arr[left] > 0:
            return arr[left]
        else:
            return 0

    Center = (left + right)/2
    MaxLeftSum = MaxSubsequenSum3(arr, left, Center)
    MaxRightSum = MaxSubsequenSum3(arr, Center+1, right)

    MaxLeftBorderSum = 0
    LeftBorderSum = 0
    i = Center
    while i >= Left:
        LeftBorderSum += arr[i]
        if LeftBorderSum > MaxLeftBorderSum:
            MaxLeftBorderSum = LeftBorderSum
        i -=1

    MaxRightBorderSum = 0
    RightBorderSum = 0
    for i in range(Center+1, Right+1):
        RightBorderSum += arr[i]
        if RightBorderSum > MaxRightBorderSum:
            MaxRightBorderSum = RightBorderSum

    return Max3(MaxLeftSum, MaxRightSum, MaxLeftBorderSum+MaxRightBorderSum)  # 返回三者中的最大者

def MaxSubsequenSum3(A):
    return MaxSubSum(A, 0, len(A)-1)




# 简单化
def MaxSubsequenSum4(arr):
    ThisSum = MaxSum = 0
    for j in range(len(arr)):
        ThisSum += arr[j]

        if ThisSum > MaxSum:
            MaxSum = ThisSum
        elif ThisSum < 0:
            ThisSum = 0
    return MaxSum
