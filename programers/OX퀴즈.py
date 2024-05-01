def solution(quiz):
    answer = []
    for qui in quiz:
        x, y, z, n, r = qui.split(" ")
        # print(x,y,z,n,r)
        if y == "+":
            y = 1
        else:
            y = (-1)
        if int(x)+int(z)*y == int(r):
            answer.append("O")
        else:
            answer.append("X")
    return answer