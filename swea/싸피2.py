from collections import deque
Test = int(input())
for num in range(1, Test+1):
    N = int(input())
    result = 0
    want = list(map(int,input().split(" ")))
    real = list(map(int,input().split(" ")))
    # want = [5, 8, 3, 4, 2, 1]
    # real = [6, 3, 7, 9, 5, 2]
    dict_a = {}
    for w in want:
        for r in real:
            if w-3 <= r <= w+3:
                if r not in dict_a:
                    dict_a[r] = [w]
                else:
                    dict_a[r].append(w)
    tar = list(dict_a.values())
    tar = sorted(tar,key=lambda x:len(x))
    for t in tar:
        wear = -111
        t = deque(sorted(t))
        if len(t) != 0:
            wear = t.popleft()
            if wear != -111:
                result += 1
            for t in tar:
                if wear in t:
                    t.remove(wear)
    print("#"+str(num)+" "+str(result))
