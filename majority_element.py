def majorityElement(nums):
    res = 0
    count = 0
    for i in nums:
        if count == 0:
            res = i
        if i == res:
            count += 1
        else:
            count -= 1
    return res
