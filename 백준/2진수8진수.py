import sys
n = sys.stdin.readline().strip()
result = []
# 11001100
temp = []

for s in n:
    temp.append(s)

while temp:
    bu = 0
    for i in range(3):
        if temp:
            a = int(temp.pop())
            if a == 1:
                bu += 2**i
    result.append(str(bu))
result.reverse()
kk = "".join(result)
print(kk)