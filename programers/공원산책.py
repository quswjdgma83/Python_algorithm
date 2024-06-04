def solution(park, routes):
    park = [[p for p in pa] for pa in park]
    a, b = 0, 0
    flag = False
    for i, pa in enumerate(park):
        for j, p in enumerate(pa):
            if "S" == p:
                a, b = i, j
                flag = True
                break
        if flag == True:
            break
    #가로: w, 세로: h
    #E[0,1], W[0,-1] S[1,0] N[-1,0]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    direct = {"E":0,"W":1,"S":2,"N":3}
    now = park[a][b]
    for route in routes:
        d,q = route.split(" ")
        k = direct[d]
        a += dx[k]*int(q)
        b += dy[k]*int(q)
        if a >= len(park) or b >= len(park[0]):
            a -= dx[k]*int(q)
            b -= dy[k]*int(q)
            continue
        if park[a][b] == "X":
            a -= dx[k]*int(q)
            b -= dy[k]*int(q)
    
    return [a,b]

solution(["OSO","OOO","OXO","OOO"],["E 2","S 3","W 1"])