from collections import deque

# 큐 생성
queue = deque()

# 큐에 요소 추가
queue.append('A')
queue.append('B')
queue.append('C')

print("큐 상태:", list(queue))

# 큐에서 요소 제거
print("제거된 요소:", queue.popleft())
print("제거된 요소:", queue.popleft())

print("최종 큐 상태:", list(queue))
