def solution(code):
    answer = ''
    ret = []
    mode = 0
    for idx in range(len(code)):
        if code[idx] == "1":
            mode = not mode
            continue
        if mode == 0:
            if idx % 2 == 0:
                ret.append(code[idx])
            else:
                continue
        elif mode == 1:
            if idx % 2 == 1:
                ret.append(code[idx])
            else:
                continue
    if ret == []:
        return "EMPTY"
    answer = "".join(ret)
        
    return answer