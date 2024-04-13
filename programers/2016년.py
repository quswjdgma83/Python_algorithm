def solution(a, b):
    answer = ''
    dal = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    d = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    # 5 3 -> 화
    day = 0
    for i in range(1,a):
        day += d[i]
    day += b
    k = day%7-3
    answer = dal[k]
    return answer