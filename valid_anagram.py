class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

'''
my original solution for this was 
'''

        # for i in s:
        #     if len(s) != len(t):
        #         return False
        #     if i in t: 
        #         continue
        #     else:
        #         return False
        # return True

'''
but this does not pass the test cases like s = 'aaba' , t = 'aabb' where no. of occurences are different '''