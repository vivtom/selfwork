# def remove_duplicate(arr):
#     seen = set()
#     array = []
#     for i in arr:
#         if i not in seen:
#             seen.add(i)
#             array.append(i)
#     return array

# result = remove_duplicate([1,2,3,2,4])
# print(result)

''' new 2025 sprint '''

class Solution(object):
    def removeDuplicates(self, nums):
        setA = set()
        i = 0
        while i < len(nums):
            if nums[i] in setA:
                nums.pop(i)
            else:
                setA.add(nums[i])
                i +=1 

        return len(nums)