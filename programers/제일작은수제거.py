def solution(arr):
    answer = []
    if len(arr) == 1:
        return [-1]
    a = min(arr)
    arr.remove(a)
    answer = arr
    return answer