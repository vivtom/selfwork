class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {')' : '(', '}' : '{', ']': '['}
        stack = []
        for i in s:
            if i in dict1:
                if stack and stack[-1] == dict1[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return False if stack else True
