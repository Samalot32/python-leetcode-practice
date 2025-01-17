from collections import defaultdict

def top_k(nums,k):
    dict = defaultdict(int)
    
    for elements in nums:
            dict[elements] += 1
          
    sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    
    top_k_elements = [item[0] for item in sorted_dict[:k]]
    
    return top_k_elements 

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)
    for num, cnt in count.items():
        freq[cnt].append(num)
    
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res

numbers=[1,1,1,2,2,3]
k=2

print(top_k(numbers,k))