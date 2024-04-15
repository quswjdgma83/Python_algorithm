def solution(n):
    ans = 0
    num = n
    while num != 0:
        if num == 1:
            ans += 1
            break
        if num % 2 == 0:
            num = num//2
        else:
            num -= 1
            ans += 1
    return ans