from collections import deque

def solution(board, moves):
    answer = 0
    # [0,0,0,0,0]
    # [0,0,1,0,3]
    # [0,2,5,0,1]
    # [4,2,4,4,2]
    # [3,5,1,3,1]
    height = len(board)
    width = len(board[0])
    moves = [i-1 for i in moves]
    new = []
    for i in range(width):
        temp = deque()
        for j in range(height):
            if board[j][i] != 0:
                temp.append(board[j][i])
        new.append(temp)
    target = []
    for i in moves:
        if new[i]:
            a = new[i].popleft()
            # print("a",a)
            if target and target[-1] == a:
                target.pop()
                answer += 2
            else:
                target.append(a)
            # print("target",target)
    return answer