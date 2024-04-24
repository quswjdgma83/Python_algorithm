def sol(num):
    temp = []
    for i in range(1,int(num**(0.5))+1):
        if num % i == 0:
            temp.append(i)
            temp.append(num//i)
    return sorted(temp)

def solution(numer1, denom1, numer2, denom2):
    answer = []
    bunmo = denom1*denom2
    bunja = numer1*denom2 + numer2*denom1
    a = sol(bunmo)
    b = sol(bunja)
    ta = 1
    for n in a:
        if n in b:
            ta = n
    return [bunja//ta,bunmo//ta]
