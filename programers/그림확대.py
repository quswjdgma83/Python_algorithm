def copy_garo(arr, k):
    bump = []
    for i in range(len(arr)):
        for _ in range(k):
            bump.append(arr[i])
    return bump

def solution(picture, k):
    answer = []
    picture = [list(pic) for pic in picture]
    y_len = len(picture[0]) #가로길이
    x_len = len(picture) #세로길이
    for i in range(len(picture)):
        a = copy_garo(picture[i], k)
        t = "".join(a)
        for _ in range(k):
            answer.append(t)

    return answer
