def productExceptSelf(nums):
    list1 = []
    
    for i in range(len(nums)):
        product = 1
        for j in range(0,len(nums)):
            if nums[j] == nums[i]:
                continue
            product *= nums[j] 
        list1.append(product)
    print(list1)
productExceptSelf([-1,0,1,2,3])
