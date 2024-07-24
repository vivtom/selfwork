def maxProfit( array):
    left = 0
    right = 1
    max_profit = 0
    while right < len(array):
        if array[right] > array[left]:
            profit = array[right] - array[left]
            max_profit = max(max_profit, profit)
        else:
            left = right
        right += 1
    return max_profit