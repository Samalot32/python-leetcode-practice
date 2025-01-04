def valid_anagram(s1,s2): #O(nlogn)
    return sorted(s1) == sorted(s2)

def valid_anagram_dict(s1,s2): #O(n^2) because of count
    return {char:s1.count(char) for char in s1} == {char:s2.count(char) for char in s2}

def valid_anagram_dict2(s1, s2):  # O(n)
    if len(s1) != len(s2):
        return False
    
    dict1, dict2 = {}, {}
    
    for char in s1:
        dict1[char] = dict1.get(char, 0) + 1
    for char in s2:
        dict2[char] = dict2.get(char, 0) + 1
    
    return dict1 == dict2

s = "racecars"
t = "carraces"

print(valid_anagram(s,t))
print(valid_anagram_dict(s,t))

print(valid_anagram_dict2(s,t))