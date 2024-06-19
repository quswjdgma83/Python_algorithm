def solution(num, total):
    answer = []
    temp = []
    for n in range(num):
        temp.append(n)
    x = (total - sum(temp))//num
    answer = [k+x for k in temp]
    return answer