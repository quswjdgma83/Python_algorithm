def solution(x):
    answer = True
    str_x = str(x)
    bump = 0
    for num in str_x:
        bump += int(num)
    if x % bump != 0:
        answer = False
    return answer