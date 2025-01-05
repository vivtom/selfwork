class Solution(object):
    def maxProfit(self, prices):
        min_el = float('inf') 
        max_el = 0
        min_index = 0
        max_index = 0
        i = 0

        while i < len(prices):
            if prices[i] < min_el:
                min_el = prices[i]
                i +=1
                min_index = i
            elif min_el == prices[len(prices)-1]:
                print(0)
            else:
                i +=1
                   
        for j in range(1, len(prices)):
            if prices[j] > max_el:
                max_el = prices[j]
                max_index = j
            else:
                continue 

        if max_index < min_index:
            return 0
        else:
            return max_el - min_el 