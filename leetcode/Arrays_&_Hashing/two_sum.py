def two_sum(nums,target): #O(n^2)
    for i in range(len(nums) - 1):
        for j in range(1, len(nums)):
            if (nums[i] + nums[j] == target and i !=j):
                return [i,j]

def two_sum_better(nums, target): #O(n)
    dict = {}
    for i,n in enumerate(nums): #Enumerate function returns the index and value(i and n in this case) of what is being enumerated (the nums array)
        diff = target - n
        if diff in dict:
            return[dict[diff], i]
        dict[n] = i
    return dict

print(two_sum([2,5,5,11], 10))
print(two_sum_better([2,5,5,11], 10))

        