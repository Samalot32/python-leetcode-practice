from collections import defaultdict

def top_k(nums,k):
    dict = defaultdict(int)
    
    for elements in nums:
            dict[elements] += 1
          
    sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    
    top_k_elements = [item[0] for item in sorted_dict[:k]]
    
    return top_k_elements 

numbers=[1,1,1,2,2,3]
k=2

print(top_k(numbers,k))