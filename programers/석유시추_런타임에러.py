import sys
sys.setrecursionlimit(10000)

# def check_oil(land, x, y):
#     count = 0
#     new_count = 0
#     x_list = []
#     new_x_list = []
#     if x < 0 or x >= len(land) or y < 0 or y >= len(land[0]) or land[x][y] == 0:
#         return 0, []
#     if land[x][y] != 0:
#         count += land[x][y]
#         land[x][y] = 0
#         x_list.append(x)
#     new_count, new_x_list = check_oil(land, x-1, y)
#     new_count, new_x_list = check_oil(land, x+1, y)
#     new_count, new_x_list = check_oil(land, x, y-1)
#     new_count, new_x_list = check_oil(land, x, y+1)
#     count += new_count
#     x_list.extend(new_x_list)
#     return count, x_list

def check_oil(land, x, y):
    count = 0
    y_list = []
    if x < 0 or x >= len(land) or y < 0 or y >= len(land[0]) or land[x][y] == 0:
        return 0, []  # 수정된 부분: 항상 튜플을 반환
    if land[x][y] != 0:
        count += land[x][y]
        land[x][y] = 0
        y_list.append(y)
    # 각 방향에 대한 재귀 호출
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_count, new_y_list = check_oil(land, x + dx, y + dy)
        count += new_count
        y_list.extend(new_y_list)
    return count, y_list

# def plus_oil(y_index, oil):
#     for y in y_index:


def solution(land):
    answer = 0
    oil_dict = {}
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] != 0:
                oil, y = check_oil(land, i, j)
                y_index = list(set(y))
                for y in y_index:
                    if y not in oil_dict:
                        oil_dict[y] = 0
                    oil_dict[y] += oil
    a = max(oil_dict.values())
        
    print(a)
    return answer

solution(
    [
        [0, 0, 0, 1, 1, 1, 0, 0], 
        [0, 0, 0, 0, 1, 1, 0, 0], 
        [1, 1, 0, 0, 0, 1, 1, 0], 
        [1, 1, 1, 0, 0, 0, 0, 0], 
        [1, 1, 1, 0, 0, 0, 1, 1]])