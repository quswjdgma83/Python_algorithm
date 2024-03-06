def separate(s):
    same = 0
    diff = 0
    first = s[0]
    for idx in range(len(s)):
        if s[idx] == first:
            same += 1
        else:
            diff += 1
        if same == diff:
            return s[idx+1:]
        elif len(s) == 1:  
            return False

def solution(s):
    answer = 0
    goal = s
    while goal:
        answer += 1
        goal = separate(goal)
    return answer

solution("abracadabra")