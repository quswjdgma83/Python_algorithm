def solution(s, n):
    answer = ''
    for ch in s:
        if ch == " ":
            answer += " "
            continue
        ch_code = ord(ch)
        if 'a' <= ch <= 'z':
            answer += chr((ch_code - 97 + n) % 26 + 97)
        elif 'A' <= ch <= 'Z':
            answer += chr((ch_code - 65 + n) % 26 + 65)
        else:
            answer += ch
    return answer

# 예시 실행
print(solution("a z A Z", 1))  # b a B A
