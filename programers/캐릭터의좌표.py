def solution(keyinput, board):
    answer = [0, 0]
    #up [0, 1]
    #down [0, -1]
    #left [-1, 0]
    #right [1, 0]
    for key in keyinput:
        if key == "up":
            if answer[1] < (board[1]-1) // 2:
                answer[1] += 1
        elif key == "down":
            if answer[1] > -(board[1]-1) // 2:
                answer[1] -= 1
        elif key == "left":
            if answer[0] > -(board[0]-1) // 2:
                answer[0] -= 1
        else:
            if answer[0] < (board[0]-1) // 2:
                answer[0] += 1
    return answer