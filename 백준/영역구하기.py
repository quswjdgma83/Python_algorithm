# 5 7 3
# 0 2 4 4
# 1 1 2 5
# 4 0 6 2
M, N, K = map(int,input().split(" "))

target = [[0]*N for _ in range(M)]

for _ in range(K):
    j1,i1,j2,i2 = map(int,input().split(" "))
    for i in range(i1,i2):
        for j in range(j1,j2):
            target[i][j] = 1
for i in range(M):
    print(target[i])