n = int(input())
result = [0]*10
for i in range(1,n+1):
    ia = str(i)
    for j in ia:
        result[int(j)] += 1
print(result)