class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        if not words:
            return 0 
        else:
            return len(words[-1])
        