class Solution(object):
    def jump(self, nums):
        l,r = 0,0 
        reachable = 0 
        while r < len(nums)-1:
            for i in range(l,r+1):
                reachable = max(reachable, i+nums[i])
                l = r+1 
                r = reachable


            return true