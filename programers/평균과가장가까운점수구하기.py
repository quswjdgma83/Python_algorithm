n = int(input())
a = list(map(int, input().split()))

ave = round(sum(a) / n) 
min_diff = float('inf') 
res = -1
score = -1 

for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min_diff:
        min_diff = tmp
        score = x
        res = idx + 1
    elif tmp == min_diff:
        if x > score:
            score = x
            res = idx + 1

print(ave, res)
