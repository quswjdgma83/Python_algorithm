key_set = set()

def keymapSearch(keymap, tar):
    a = []
    for key in keymap:
        key = list(key)
        if tar in key:
            a.append(key.index(tar)+1)
    k = min(a)
    return k

    return a

def solution(keymap, targets):
    answer = []
    #1. 존재하는가?
    for st in keymap:
        for s in st:
            key_set.add(s)
    count = 0

    for target in targets:
        flag = True
        for tar in target:
            if tar not in key_set:
                flag = False
                continue
            count += keymapSearch(keymap, tar)
        if flag == True:
            answer.append(count)
        if flag == False:
            answer.append(-1)
        count = 0
        print(answer)
    return answer

solution(["ABACD", "BCEFD"],["ABCD","AABB"])
