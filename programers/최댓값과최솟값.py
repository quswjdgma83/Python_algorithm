def solution(s):
    answer = ''
    tar = s.split(" ")
    tar = [int(i) for i in tar]
    k = sorted(tar)
    # print(k)
    answer = str(k[0])+ " "+str(k[-1])
    return answer