from collections import deque

def solution(storey):
    answer = 0
    numbers = deque([int(st) for st in str(storey)])
    numbers.reverse()
    while len(numbers) != 0:
        temp = numbers.popleft()
        if len(numbers) == 0:
            if temp == 10:
                answer += 1
                break
            elif temp >= 6:
                answer += 10-temp
                break
            else:
                answer += temp
                break
        if temp == 10:
            numbers[0] += 1
            continue
        elif temp >= 6:
            answer += (10-temp)
            numbers[0] += 1
        elif temp <= 4:
            answer += temp
        elif temp == 5:
            a = numbers[0]
            if a >= 5:
                answer += (10 - temp)
                numbers[0] += 1
            else:
                answer += temp
    return answer

solution(999)