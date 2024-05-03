from collections import deque

def leng(deq):
    temp = set(deq)
    cnt = len(temp)
    return cnt

def solution(topping):
    answer = -1
    center = 0
    left = deque(topping[:center])
    right = deque(topping[center:])

    cnt = 0
    flag = False
    for _ in range(len(topping)):
        if cnt != 0 and flag == False:
            # print("left",left)
            # print("right",right)
            print("dd")
            break
        if leng(left) < leng(right):
            a = right.popleft()
            left.append(a)
            flag = False
            continue
        elif leng(left) == leng(right):
            cnt += 1
            flag = True
            # print("left",left)
            # print("right",right)
            a = right.popleft()
            left.append(a)
        else:
            flag = False

        # print("left",left)
        # print("right",right)
    answer = cnt
    return answer

solution([1, 2, 1, 3, 1, 4, 1, 2])