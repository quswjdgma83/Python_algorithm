N = int(input())

for i in range(1,N+1):
    result = 0
    a,b,c = map(int,input().split(" "))
    if c < 3 or min([a,b,c]) == 0 or b == 1:
        result = -1
        print("#"+str(i)+" "+str(result))
        continue
    if a < b < c:
        print("#" + str(i) + " 0")
        continue
    two = c-1
    if two > b:
        two = b
    else:
        result += (b - two)
    three = two-1
    if three > c:
        three = c
    else:
        result += (a - three)
    print("#"+str(i)+" "+str(result))