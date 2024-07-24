def solution(polynomial):
    answer = ''
    pol = polynomial.split(" ")
    a, b = 0, 0
    for p in pol:
        if p != '+':
            if 'x' in p:
                if p == 'x':
                    a += 1
                else:
                    a += int(p[:-1])
            else:
                b += int(p)
                
    if a != 0:
        if a == 1:
            answer = 'x'
        else:
            answer = str(a) + 'x'
    if b != 0:
        if a != 0:
            answer += ' + ' + str(b)
        else:
            answer = str(b)
    return answer
