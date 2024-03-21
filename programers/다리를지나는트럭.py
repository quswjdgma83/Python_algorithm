from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    wait = deque(truck_weights)
    ongoing = deque([0 for _ in range(bridge_length)])
    ongoing2 = deque()
    arrived = deque()
    flag = False
    while len(arrived) != len(truck_weights):
        truck_out = ongoing.popleft()
        #다리 출구 톨게이트
        if truck_out != 0:
            ongoing2.popleft()
            arrived.append(truck_out)
        #다리 진입조건
        if len(wait) > 0 and (weight - sum(ongoing2)) >= wait[0] and len(ongoing2) < bridge_length:
            flag = True
        else:
            flag = False
        #출발
        if flag == True:
            truck_in = wait.popleft()
            ongoing.append(truck_in)
            ongoing2.append(truck_in)
        else:
            ongoing.append(0)
        time += 1
    return time