# 三数之和

def threeSum(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    for i, v in enumerate(nums[:-2]):
        if i >= 1 and v == nums[i-1]:
            continue
        d = {}
        for x in nums[i+1:]:
            if x not in d:
                d[-v-x] = 1
            else:
                res.add((v, -v-x, x))
    return list(map(list, res))

nums = [-1, 0, 1, 2, -1, -4]
# print(threeSum(nums))








def threeSum2(nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1  # 左右边界
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1

print(threeSum2(nums))
