def calc(f,t):
    a = abs(f[0]-t[0])
    b = abs(f[1]-t[1])
    return a+b
    
def solution(numbers, hand):
    answer = ''
    # 왼: 1, 4, 7
    # 오: 3, 6, 9
    # 가: 2, 5, 8, 0
    dict_a = {
        1: (0,0),
        2: (0,1),
        3: (0,2),
        4: (1,0),
        5: (1,1),
        6: (1,2),
        7: (2,0),
        8: (2,1),
        9: (2,2),
        0: (3,1)
    }
    dict_b = {
        "left": "L",
        "right": "R"
    }
    left = (3,0)
    right = (3,2)
    for num in numbers:
        if num in [1,4,7]:
            answer += "L"
            left = dict_a[num]
        elif num in [3, 6, 9]:
            answer += "R"
            right = dict_a[num]
        else:
            l = calc(left, dict_a[num])
            r = calc(right, dict_a[num])
            if l == r:
                answer += dict_b[hand]
                if hand == "left":
                    left = dict_a[num]
                else:
                    right = dict_a[num]
            elif l > r:
                answer += "R"
                right = dict_a[num]
            else:
                answer += "L"
                left = dict_a[num]
    return answer