def solution(a, b, c, d):
    diceDict = {}

    temp = [a, b, c, d]
    bump = []
    for num in temp:
        if num not in diceDict:
            diceDict[num] = 0
        diceDict[num] += 1
        sorted_dict = sorted(diceDict.items(), key=lambda item: item[1], reverse=True)
        diceDict = dict(sorted_dict)
    if(len(diceDict) == 4):
        return min(diceDict)
    elif(len(diceDict) == 3):
        bump = list(diceDict.keys())
        q = bump[1]
        r = bump[2]
        return q*r
    elif(len(diceDict) == 2):
        if min(diceDict.values()) != 1:
            bump = list(diceDict.keys())
            p = bump[0]
            q = bump[1]
            return (p+q)*abs(p-q)
        else:
            bump = list(diceDict.keys())
            p = bump[0]
            q = bump[1]
            return (10*p+q)**2
    else:
        bump = list(diceDict.keys())
        p = bump[0]
        return 1111*p