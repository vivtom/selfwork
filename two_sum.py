class Solution(object):
    def twoSum(self, nums, target):
        dict1 = {}
        for i,n in enumerate (nums):
            var1 = target - n
            if  var1 in dict1:
                return [i and dict1[var1]]
            else:
                dict1[n] = i