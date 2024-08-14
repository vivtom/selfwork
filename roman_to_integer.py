class Solution(object):
    def romanToInt(self, s):
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range (len(s)):
            if i+1 < len(s) and roman_values[s[i+1]] > roman_values[s[i]]:
                res -= roman_values[s[i]]
            else:
                res += roman_values[s[i]]
        return res 
