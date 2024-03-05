def exchange(n, a, b):
    f = (n // a)*b #꽉찬 콜라
    nu = n % a # 빈병
    return f, nu

def solution(a, b, n):
    # 빈병 a개, a개 미만이면 안바꿔줌
    # 콜라 빈병 a병을 b병으로 바꿔줌
    # 가져가는 빈병 수: n
    answer = 0
    coke_bottle = n
    coke_full = 0
    while coke_bottle >= a:
        coke_full, nu = exchange(coke_bottle, a, b)
        coke_bottle = coke_full + nu
        answer += coke_full

    print(answer)
    return answer

solution(2, 1, 20)
# a	b	n	result
# 2	1	20	19