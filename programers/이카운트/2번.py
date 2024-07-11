import itertools

def sliding_window_sum(iterable, n):
    it = iter(iterable)
    window = list(itertools.islice(it, n))
    if len(window) == n:
        sum_window = sum(window)
        yield sum_window
    for e in it:
        sum_window += e - window.pop(0)
        window.append(e)
        yield sum_window

# 예술품 종류: N, 최소: L, 최대: R
N, L, R = map(int, input().split())
target = list(map(int, input().split()))

answer = 0
for n in range(1, N + 1):
    for sum_window in sliding_window_sum(target, n):
        if L <= sum_window <= R:
            answer += 1
print(answer)
