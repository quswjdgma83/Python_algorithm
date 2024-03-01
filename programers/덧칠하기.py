def solution(n, m, section):
    temp = [1 for _ in range(n)]
    count = 0
    for sect in section:
        temp[sect-1] = 0
    def ssg(m, temp, idx, count):
        bump = [1 for _ in range(m)]
        temp[idx:idx+m] = bump
        return temp
    while 0 in temp:
        ssg(m, temp, temp.index(0), count)
        count += 1
    answer = count
    return answer