from math import sqrt


def gop(num):
    dict_a = {}
    for i in range(1,int(sqrt(num))+1):
        if num % i == 0:
            dict_a[i] = num//i
    return dict_a

def solution(brown, yellow):
    yx, yy = 0, 0
    dict_k = gop(yellow)
    for key in dict_k:
        if(key + dict_k[key] == (brown-4)//2):
            yx = key
            yy = dict_k[key]
            break
    if yy > yx:
        yx, yy = yy, yx
    return [yx+2,yy+2]