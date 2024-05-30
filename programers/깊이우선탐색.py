def dfs(hap, now, numbers, target):
    if now == len(numbers)-1:
        if hap == target:
            return 1
        return 0
        
    case1 = dfs(hap+numbers[now+1],now+1, numbers, target)
    case2 = dfs(hap-numbers[now+1],now+1, numbers, target)
    # print(case1, case2)
    return case1 + case2

def solution(numbers, target):
    answer = 0
    answer = dfs(numbers[0], 0,numbers,target) + dfs(-numbers[0], 0,numbers,target)
    
    return answer

solution([1, 1, 1, 1, 1],3)