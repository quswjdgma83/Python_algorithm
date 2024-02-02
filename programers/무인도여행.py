import sys
sys.setrecursionlimit(10000)

def dfs(maps, x, y):
    if x < 0 or x >= len(maps) or y < 0 or y >= len(maps[0]) or maps[x][y] == 'X':
        return 0
    food = int(maps[x][y])
    maps[x][y] = 'X'  # 방문한 칸은 'X'로 변경하여 중복 탐색을 방지
    # 상하좌우 탐색
    food += dfs(maps, x-1, y)
    food += dfs(maps, x+1, y)
    food += dfs(maps, x, y-1)
    food += dfs(maps, x, y+1)
    return food

def solution(maps):
    # 문자열의 리스트를 문자 리스트의 리스트로 변환
    maps = [list(row) for row in maps]
    days = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X':
                days_on_island = dfs(maps, i, j)
                if days_on_island > 0:
                    days.append(days_on_island)
    if not days:
        return [-1]
    return sorted(days)


