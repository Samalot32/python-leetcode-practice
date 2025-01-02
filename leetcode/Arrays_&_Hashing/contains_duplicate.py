def contains_dup(arr):
    dictionary = {}
    
    for i in range(len(arr) - 1):
        if i in dictionary:
            return True
        else:
            dictionary = arr[i]
    print(arr)
    return False

nums = [1,2,3,4,3,6]

print(contains_dup(nums))