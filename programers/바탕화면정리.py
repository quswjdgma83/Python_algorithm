def solution(wallpaper):
    # 빈칸은 ".", 파일이 있는 칸은 "#"
    sx, sy, ex, ey = 0, 0, 0, 0
    x, y = [], []
    b = 0
    for i, wa in enumerate(wallpaper):
        for j, w in enumerate(wa):
            if w == "#":
                x.append(j)
                y.append(i)
    # print(x)
    # print(y)
    sx = min(x)
    sy = min(y)
    ex = max(x)
    ey = max(y)
    answer = [sy,sx,ey+1,ex+1]
    return answer