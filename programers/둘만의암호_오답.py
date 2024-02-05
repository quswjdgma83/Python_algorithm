def solution(s, skip, index):
    # a: 97 (-97 하면 0), z: 122 (-97하면 25)
    answer = ''
    s_list = []
    skip_list = []
    #스킵리스트
    for i in range(len(skip)):
        bump = ord(skip[i])
        skip_list.append(bump)
    #목표 리스트
    for i in range(len(s)):
        bump = ord(s[i])
        s_list.append(bump)   
        #index처리
        plus = 0
        for j in range(1, index+1):
            a = s_list[i] + j
            if a in skip_list:
                plus += 2
            else:
                plus += 1
        s_list[i] += plus
        if s_list[i] > 122:
            # 123 -> a(97) 125 -> c(99)
            s_list[i] = (s_list[i]-97) % 26 + 97
    for i in range(len(s)):
        answer += chr(s_list[i])
    
    return answer