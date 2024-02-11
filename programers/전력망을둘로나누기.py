def solution(n, wires):
    answer = -1
    tower_dict = {}
    towers = [i for i in range(1,n+1)]
    #wire해체
    bump = []
    for a, b in wires:
        bump.append(a)
        bump.append(b)
    #dict생성
    for tower in towers:
        tower_dict[tower] = 0
    #dict구성
    for tower in bump:
        for key in tower_dict:
            if key == tower:
                tower_dict[key] += 1
    print(tower_dict)
    return answer

solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])
solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])
# 73페이지
{1: 1, 
 2: 1, 
 3: 3, 
 4: 4, 
 5: 1, 
 6: 1, 
 7: 3, 
 8: 1,
 9: 1}

{1: 1, 
 2: 2, 
 3: 2, 
 4: 2, 
 5: 1, 
 6: 1, 
 7: 3}