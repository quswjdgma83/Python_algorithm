for k in range(10):
    N = int(input())
    bds = list(map(int,input().split(" ")))
 
    answer = 0
    leng = len(bds)
    for i, bd in enumerate(bds):
        temp = []
        if 2 <= i <= (leng - 2):
            temp = bds[i-2:i] + bds[i+1:i+3]
            top = max(temp)
            if top < bd:
                answer += (bd - top)
 
    print("#"+str(k+1)+" "+str(answer))