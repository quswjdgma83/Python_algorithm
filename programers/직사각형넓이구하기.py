def solution(dots):
    answer = 0
    x = []
    y = []
    for dot in dots:
        x.append(dot[0])
        y.append(dot[1])
    x = sorted(x)
    y = sorted(y)
    answer = (x[2]-x[1])*(y[2]-y[1])

    return answer