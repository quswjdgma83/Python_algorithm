def mktw(n, k):
    temp = []
    while n != 1 and n != 0:
        if n % 2 == 0:
            temp.append("0")
            n = n // 2
        elif n % 2 == 1:
            temp.append("1")
            n = n // 2
    if n == 0:
        temp.append("0")
    else:
        temp.append("1")
    if len(temp) != k:
        while len(temp) != k:
            temp.append("0")
    temp = reversed(temp)
    a = ""
    for t in temp:
        a += t
    return a

def solution(n, arr1, arr2):
    answer = []
    ar1 = []
    ar2 = []
    temp = ""
    for a1 in arr1:
        ar1.append(mktw(a1,n))
    for a2 in arr2:
        ar2.append(mktw(a2,n))
    
    for i in range(len(ar1)):
        temp = ""
        for j in range(n):
            if ar1[i][j] == "1" or ar2[i][j] == "1":
                temp += "#"
            else:
                temp += " "
        answer.append(temp) 
    return answer