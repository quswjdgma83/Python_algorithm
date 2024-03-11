def solution(s):
    #banana
    s = list(s)
    s_set = set(s)
    for ch in s_set:
        flag = False
        index = 0
        for idx in range(len(s)):
            if s[idx] == ch:
                #처음일 떄
                if flag == False:
                    s[idx] = -1
                    flag = True
                    index = idx
                #구면일 때
                else:
                    s[idx] = idx - index
                    index = idx
    print(s)
    return s

# [-1, -1, -1, 2, 2, 2]
solution("banana")