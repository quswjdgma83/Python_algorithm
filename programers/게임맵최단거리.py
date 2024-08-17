def solution(maps):
    answer = 0
    dy = [1,0,-1,0]
    dx = [0,-1,0,1]
    # 동, 북, 서, 남
    x, y = 0, 0
    my = maps[x][y]
    while True:
        f_count = 0
        if x >= 0 and y >= 0 and y < 5 and x < 5:
            # print(x, y)
            for i in range(4):
                print(x+dx[i], y+dy[i])
                print(maps[x+dx[i]][y+dy[i]] == 1)
                if maps[x+dx[i]][y+dy[i]] == 1:
                    maps[x][y] = 0
                    x += dx[i]
                    y += dy[i]
                    answer += 1
                else:
                    f_count += 1
                    if f_count == 4 and (x, y) != (4,4):
                        return -1
        else:
            break
            
    
    
    return answer