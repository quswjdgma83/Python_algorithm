ALPHABET = {
'A': 0,'B': 1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,
'K':10,'L':11,'M':12,'N':13,'O':12,'P':11,'Q':10,'R':9,'S':8,
'T':7,'U':6,'V':5,'W':4,'X':3,'Y':2,'Z':1}


def solution(name):
    answer = 0
    reversedName = "".join(reversed(name[1:]))
    count_L = 0
    count_R = 0
    count_A1 = 0
    count_A2 = 0
    for A in name:
        answer += ALPHABET[A]
    name = name[1:]
    for R in name:
        if R == "A":
            count_A1 += 1
        if R != "A":
            count_R += count_A1
            count_A1 = 0
            count_R += 1
    for L in reversedName:
        if L == 'A':
            count_A2 += 1
        if L != "A":
            count_L += count_A2
            count_A2 = 0
            count_L += 1
    answer += min(count_L, count_R)
    print(answer)
    return answer

# solution("JEROEN") =>6 5
# solution("JAAN") =>4 2
# solution("BAAAAB")
solution("LOAAAHAJAAFAEBAWO")
# "BAAAAB"
# input:LOAAAHAJAAFAEBAWO / answer:79

def solution2(name):
    answer = 0
    n = len(name)
    min_move = n - 1
    
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        next = i + 1
        while next < n and name[next] == 'A':
            next += 1
            
        distance = min(i, n - next)
        min_move = min(min_move, i + n - next + distance)
        
    answer += min_move
    print(answer)
    return answer

solution2("LOAAAHAJAAFAEBAWO")