def largest_prod_subarray(nums):
    if len(nums) < 2:
            return nums[0]
    max_prod = nums[0]
    for i in range(len(nums)):
        prod = nums[i]
        for j in range(i, len(nums)):
            if i == j:
                prod = nums[j]
            else:
                prod *= nums[j]
            if prod > max_prod:
                max_prod = prod
    return max_prod

test1 = [0,1]
print(largest_prod_subarray(test1))

test2 = [-3, -2, 3, -1, -1]
print(largest_prod_subarray(test2))

test3 = [-2, -2]
print(largest_prod_subarray(test3))
