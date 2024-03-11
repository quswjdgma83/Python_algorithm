def solution(s):
    s_dict = {"zero":"0",
            "one": "1",
            "two":"2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"}
    answer = ""
    temp = ""
    for ch in s:
        if ch not in list(s_dict.values()):
            temp += ch
            if temp in list(s_dict.keys()):
                answer += s_dict[temp]
                temp = ""
        else:
            answer += ch
    answer = int(answer)
    return answer

solution("one4seveneight")