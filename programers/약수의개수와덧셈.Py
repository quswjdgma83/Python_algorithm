def make_list(number):
    list = []
    for num in range(1, number+1):
        list.append(num)
    return list

def solution(left, right):
    answer = 0
    for number in range(left, right+1):
        bump = make_list(number)
        print(bump) 
    return answer
