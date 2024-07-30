LH = '*'
RH = '#'

def compare(num, L, R, hand):
    global LH, RH
    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2),
              '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    
    Cind = keypad[num]
    Lind = keypad[L]
    Rind = keypad[R]
    
    Ldist = abs(Cind[0] - Lind[0]) + abs(Cind[1] - Lind[1])
    Rdist = abs(Cind[0] - Rind[0]) + abs(Cind[1] - Rind[1])
    
    if Ldist == Rdist:
        if hand == "left":
            LH = num
            return "L"
        else:
            RH = num
            return "R"
    if Ldist < Rdist:
        LH = num
        return "L"
    else:
        RH = num
        return "R"

def solution(numbers, hand):
    global LH, RH
    answer = ''
    hand = "left" if hand == "left" else "right"
    
    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            LH = num
        elif num in [3, 6, 9]:
            answer += "R"
            RH = num
        else:
            answer += compare(num, LH, RH, hand)
                
    return answer
