def copy_garo(arr):
    bump = []
    for i in range(len(arr)):
        bump.append(arr[i])
        bump.append(arr[i])
    return bump

def solution(picture, k):
    answer = []
    picture = [list(pic) for pic in picture]
    y_len = len(picture[0]) #가로길이
    x_len = len(picture) #세로길이
    # answer = [[0 for _ in range(y_len*2)] for _ in range(x_len*2)]
    for i in range(len(picture)):
        a = copy_garo(picture[i])
        k = "".join(a)
        answer.append(k)
        answer.append(k)

    return answer
