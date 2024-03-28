from math import factorial

def solution(n):
    answer = 0
    temp = n
    dict_a = {}
    two = 0
    while temp != -2 and temp != -1:
        dict_a[temp] = two
        two += 1
        temp -= 2
    for key in dict_a:
        a = key+dict_a[key]
        if key == n:
            answer += 1
        else:
            answer += factorial(key+dict_a[key])//(factorial(key)*factorial(dict_a[key]))
    answer = answer%1234567
    return answer