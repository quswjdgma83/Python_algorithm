def bangmun(dict_a, n):
    next, b = dict_a[n]
    if b == True:
        return n, "stop"
    else:
        dict_a[n] = (next, True)
        return n, next

def solution(cards):
    answer = 0
    # index[1,2,3,4,5,6,7,8]
    # cards[8,6,3,7,2,5,1,4]
    dict_a = {}
    dec = [c-1 for c in cards]
    print(cards)
    
    i = 0
    for card in dec:
        dict_a[card] = (i,False)
        i+= 1
    print(dict_a)
    cnt = 0
    for i in range(len(dec)):
        n = i
        print(i)
        while True:
            if len(dec) == 0:
                return 0
            n, next = bangmun(dict_a,n)
            if next == "stop":
                break
            else:
                cnt += 1
                dec.remove(n)
                bangmun(dict_a, next)
            print(dec)
    


    return answer

solution([8,6,3,7,2,5,1,4])
# [7,5,2,6,1,4,0,3]
# [0,1,2,3,4,5,6,7]