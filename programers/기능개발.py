from collections import deque

def solution(progresses, speeds):
    answer = []
    speed = deque(speeds)
    process = deque(progresses)
    while(len(process) != 0):
        count = 0
        #process 비우는 작업
        if process[0] >= 100:
            while(len(process)>0 and process[0] >= 100):
                process.popleft()
                speed.popleft()
                count += 1
            answer.append(count)
            
        for i in range(len(process)):
            process[i] += speed[i]
    print(answer)
    return answer

solution([93, 30, 55], [1, 30, 5])