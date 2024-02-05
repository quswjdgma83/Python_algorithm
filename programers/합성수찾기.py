def solution(n):
    #1,2,4
    #1,2,3,6
    #1,2,4,8
    #1,3,9
    #1,2,5,10
    answer = 0
    result = 0
    numList = [num for num in range(1,n+1)]
    
    for k in range(1, n+1):
        count = 0
        #n이라는 숫자의 약수 개수 구하는 블록 
        for i in range(k):
            if k % numList[i] == 0:
                count += 1
        if count > 2:
            result += 1
    return result

solution(10)