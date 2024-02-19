def solution(my_string, overwrite_string, s):
    goal = len(overwrite_string)
    bump = list(my_string)
    for idx in range(s, s+ goal):
        bump[idx] = overwrite_string[idx-s]
    answer = "".join(bump)
    
    return answer