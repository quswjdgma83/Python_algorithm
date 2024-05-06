def solution(n):
    answer = 0
    fibo = [0,1]
    for i in range(2,n+1):
        a0, a1 = fibo[i-2], fibo[i-1]
        fibo.append(a0+a1)
    answer = fibo[-1] % 1234567
    return answer