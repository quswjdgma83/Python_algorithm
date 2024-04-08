a, b = list(map(int, input().split()))

def sol(n):
    i = 2
    temp = []
    while(True):
        if n == 1:
            return temp
            break
        if n % i == 0:
            n = n//i
            temp.append(i)
            i = 2
        else:
            if i == n:
                return [1,n]
            i += 1

kk = sol(a)
print(kk)