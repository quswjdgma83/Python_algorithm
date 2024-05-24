def solution(cipher, code):
    answer = ''
    for i, j in enumerate(cipher):
        if (i+1) % code == 0:
            answer += j
    return answer