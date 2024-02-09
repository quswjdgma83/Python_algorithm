def solution(n):
    answer = []
    # 방향: 우, 하, 좌, 상
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    square = [[0 for _ in range(n)]for _ in range(n)]
    x, y = 0, 0
    toward = 0
    count = 1
    for _ in range(n*n):
        square[x][y] = count
        
        nx = x + dx[toward]
        ny = y + dy[toward]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or square[nx][ny] != 0:
            toward = (toward+1) % 4
            nx = x + dx[toward]
            ny = y + dy[toward]
        x, y = nx, ny
        count += 1
            

    return answer

solution(4)