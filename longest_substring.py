class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1 = set()
        l = 0 
        max_count = 0
        for r in range(len(s)):
            while s[r] in set1:
                set1.remove(s[l])
                l +=1 
            set1.add(s[r])
            max_count = max(max_count,(r-l)+1)
        return max_count
