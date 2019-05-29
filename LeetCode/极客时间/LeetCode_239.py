def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # 判断传入值
    if not nums: return []
    window, res = [], []
    for i, x in enumerate(nums):
        if i >= k and window[0] <= i - k:
            window.pop(0)
        while window and nums[window[-1]] <= x:  # 对新进入的元素
            window.pop()
        window.append(i)
        if i >= k - 1:
            res.append(nums[window[0]])
    return res
