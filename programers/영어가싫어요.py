def solution(numbers):
    answer = 0
    dict_a = {
        "zero": "0", "one": "1", "two": "2", "three":"3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    # print(dict_a.keys())
    A = list(dict_a.keys())
    temp1 = ""
    temp2 = ""
    for num in numbers:
        temp1 += num
        if temp1 in A:
            temp2 += dict_a[temp1]
            temp1 = ""
    print(temp2)
    answer = int(temp2)
    return answer