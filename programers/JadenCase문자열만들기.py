def solution(s):
    answer = ''
    s = s.lower()
    temp = s.split(" ")
    for te in range(len(temp)):
        for i in range(len(temp[te])):
            char = ord(temp[te][i])
            if i == 0:
                if not (char >= 97 and char <= 122) or (char >= 65 and char <= 90):
                    answer += chr(char)
                    continue
                else:
                    a = char-32
                    answer += chr(a)
            else:
                answer += temp[te][i]
        if te != len(temp)-1:
            answer += " "
    # answer[len(anwer)]
    return answer