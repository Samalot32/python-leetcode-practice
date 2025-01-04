from collections import defaultdict

def group_anagrams(strs):
    dict = defaultdict(list)    
    
    for string in strs:
        dict[sorted(string).append(string)]

    return list(dict.values())

def group_anagrams_better(strs): #O(m * n)
    dict = defaultdict(list)    
    
    for string in strs:
        count = [0] * 26

        for c in string:
            count[ord(c) - ord("a")] += 1
        dict[tuple(count)].append(string)
        
    return list(dict.values())

strs = ["act","pots","tops","cat","stop","hat"]
print(group_anagrams_better(strs))