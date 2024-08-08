def solution(park, routes):
    #E: 0 1
    #N:-1 0
    #W: 0 -1
    #S: 1 0
    x, y = 0, 0
    for i, pa in enumerate(park):
        c = 0
        for p in pa:
            if p == "S":
                x, y = i, int(c)
            c += 1
    for order in routes:
        direct = order[0]
        quant = int(order[2])
        if direct == "E":
            count = 0
            for _ in range(quant):
                if y < len(park[0])-1 and park[x][y+1] != "X" :
                    y += 1
                    count += 1
                else:
                    y -= count
                    break
        elif direct == "N":
            count = 0
            for _ in range(quant):
                if x > 0 and park[x-1][y] != "X":
                    x -= 1
                    count += 1
                else:
                    x += count
                    break
        elif direct == "W":
            count = 0
            for _ in range(quant):
                if y > 0 and park[x][y-1] != "X":
                    y -= 1
                    count += 1
                else:
                    y += count
                    break
        elif direct == "S":
            count = 0
            for _ in range(quant):
                if x < len(park)-1 and  park[x+1][y] != "X":
                    x += 1
                    count += 1
                else:
                    x -= count
                    break
        print(direct, quant, x, y)
    return [x,y]