import sys
sys.setrecursionlimit(100000)

y_list_set = set()

def check_oil(land, x, y):
    if x < 0 or y < 0 or x >= len(land) or y >= len(land[0]) or land[x][y] == 0:
        return 0
    count = 0
    count += land[x][y]
    land[x][y] = 0
    y_list_set.add(y)
    for dx, dy in [(0,1),(0,-1),(-1,0),(1,0)]:
        count += check_oil(land, x+dx, y+dy)
    return count

def solution(land):
    oil_dict = {key: 0 for key in range(len(land[0]))}
    answer = 0
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] != 0:
                oil = check_oil(land, i, j)
                for y in y_list_set:
                    oil_dict[y] += oil
                y_list_set.clear() 
    answer = max(oil_dict.values())
    return answer
solution(
    [
        [0, 0, 0, 1, 1, 1, 0, 0], 
        [0, 0, 0, 0, 1, 1, 0, 0], 
        [1, 1, 0, 0, 0, 1, 1, 0], 
        [1, 1, 1, 0, 0, 0, 0, 0], 
        [1, 1, 1, 0, 0, 0, 1, 1]])