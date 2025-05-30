#   O(n^2) approach using 2 pointers (not very efficient)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0 
        r = 1
        while l < len(nums) - 1:
            if r >= len(nums):
                l += 1
                r = l + 1
            elif nums[l] == nums[r]:
                if (r - l) <= k:
                    return True
                else:
                    l += 1
                    r = l + 1
            else:
                r += 1
        return False