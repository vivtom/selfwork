# class Solution(object):
def canJump(nums):
    i = 0
    while i < len(nums):
        i += nums[i]
        if i == len(nums)-1:
            return True
        else:
            return False
res = canJump([3,2,1,0,4])
print(res)