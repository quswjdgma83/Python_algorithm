from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    NP = 0
    while(len(prices)!=0):
        count = 0
        NP = prices.popleft()
        if len(prices) != 0:
            flag = False
            for pp in prices:
                if NP > pp:
                    count += 1
                    break
                else:
                    count += 1
            answer.append(count)
        else:
            answer.append(0)
    return answer