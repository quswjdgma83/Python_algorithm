count = 0

def hamsu(arr):
    bump = [ num for num in arr ]
    for i in range(len(arr)):
        if arr[i] >= 50 and arr[i] % 2 == 0:
            bump[i] = bump[i] // 2
        if arr[i] < 50 and arr[i] % 2 == 1:
            bump[i] = bump[i] * 2 + 1
    return bump

def recursion(arr):
    global count
    result = hamsu(arr)
    if arr == result:
        return count  # 재귀 호출이 종료될 때 count 값을 반환
    else:
        count += 1
        return recursion(result)

def solution(arr):
    answer = recursion(arr)
    print(answer)
    return answer
    
solution([1, 2, 3, 100, 99, 98])