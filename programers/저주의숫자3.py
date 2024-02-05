def solution(n):
    answer = 0
    bg_number = []
    number = 1
    for i in range(1, n + 1):
        str_num = str(number)
        if number % 3 != 0 and "3" not in str_num:
            bg_number.append(number)
            number += 1
        else:
            while (not(number % 3 != 0 and "3" not in str_num)):
                number += 1
                str_num = str(number)
            bg_number.append(number)
            number += 1
    n = len(bg_number)
    print(bg_number)
    answer = bg_number[n - 1]
    return answer