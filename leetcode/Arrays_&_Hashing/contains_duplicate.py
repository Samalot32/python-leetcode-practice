def contains_dup(arr):
    dictionary = {}
    
    for num in arr:
        if num in dictionary:
            return True
        dictionary[num] = 1
    return False

def contains_dup_length(arr):
    return len(set(arr)) < len(arr)

array = [1,2,3,4,5,6,5]

print(contains_dup(array))
print(contains_dup_length(array))

print(max(6,2))