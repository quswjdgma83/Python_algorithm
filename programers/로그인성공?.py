def solution(id_pw, db):
    ID, PW = 0, 0
    dict_a = {}
    for d in db:
        ID, PW = d[0], d[1]
        dict_a[ID] = PW
    a, b = id_pw[0], id_pw[1]
    if a not in list(dict_a.keys()):
        return "fail"
    elif dict_a[a] == b:
        return "login"
    else:
        return "wrong pw"