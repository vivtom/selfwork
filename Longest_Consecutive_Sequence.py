class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        max_val = 1
        current_val = 1
        
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == (nums[i-1]+1):
                current_val += 1
            else:
                max_val = max(max_val, current_val)
                current_val = 1
        return max(max_val,current_val)
    
'''
O(n) approach 
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:  # start of a sequence
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)

        return longest