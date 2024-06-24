def solution(todo_list, finished):
    answer = []
    for i, tl in enumerate(todo_list):
        if finished[i] == False:
            answer.append(tl)
    return answer