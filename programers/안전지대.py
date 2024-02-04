def make_bumpBoard(board):
    board_size = len(board)
    bump_board = [[0 for i in range(board_size+2)] for i in range(board_size+2)]

    for i in range(board_size):
        for j in range(board_size):
            bump_board[i+1][j+1] = board[i][j]
    return bump_board

def make_danger_zone(board, x, y):
    if board[x][y] == 'X' or board[x][y] ==0:
        return board[x][y]
    if board[x][y] == 1:
        if board[x-1][y-1] != 1:
            board[x-1][y-1] = 'X'
        if board[x-1][y] != 1:
            board[x-1][y] = 'X'
        if board[x-1][y+1] != 1:
            board[x-1][y+1] = 'X'
        if board[x][y-1] != 1:
            board[x][y-1] = 'X'
        if board[x][y+1] != 1:
            board[x][y+1] = 'X'
        if board[x+1][y-1] != 1:
            board[x+1][y-1] = 'X'
        if board[x+1][y] != 1:
            board[x+1][y] = 'X'
        if board[x+1][y+1] != 1:
            board[x+1][y+1] = 'X'
    return board


def solution(board):
    answer = 0
    # 큰 보드에 복사
    bump = make_bumpBoard(board)
    for i in range(1, len(bump)-1):
        for j in range(1, len(bump)-1):
            make_danger_zone(bump, i, j)
    for i in range(1, len(bump)-1):
        for j in range(1, len(bump)-1):
            if bump[i][j] == 0:
                answer += 1
    print(bump)
    return answer


def solution(board):
    n = len(board)
    zone = [[0 for _ in range(n)] for _ in range(n)]
    dx = [0, -1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, 0, -1, 1, -1, 1, -1, 1]

    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                for i in range(9):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        zone[nx][ny] = 1

    answer = 0
    for z in zone:
        answer += z.count(0)
    return answer
