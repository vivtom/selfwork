# O(n) approach
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        set1 = set()
        l = 0
        for r in range(len(nums)):
            if (r-l) > k:
                set1.remove(nums[l])
                l +=1 
            if nums[r] in set1:
                return True
            set1.add(nums[r])
        return False


#   O(n^2) approach using 2 pointers (not efficient, ignore)
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
    
