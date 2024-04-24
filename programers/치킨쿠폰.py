def solution(chicken):
    service = 0
    chick = chicken
    while True:
        if chick >= 10:
            chick -= 10
            service += 1
            chick += 1
        else:
            break
    return service