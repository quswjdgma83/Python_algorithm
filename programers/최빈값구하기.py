from collections import defaultdict

def solution(array):
    answer = 0
    dict_a = defaultdict(int)
    
    for arr in array:
        dict_a[arr] += 1
    a = list(dict_a.values())
    b = max(a)
    if a.count(b) > 1:
        return -1
    else:
        keys = [key for key, value in dict_a.items() if value == b]
        answer = keys[0]
    return answer