comma = ","
tt = ["{","}"]

def solution(s):
    answer = []
    bp = []
    temp = []
    target = s[1:len(s)-1]
    print(target)
    flag = False
    k = ""
    for string in target:
        if string == "{":
            flag = True
        elif string == "}":
            flag = False
        if flag == True and string != "{":
            if string != comma:
                k += string
            else:
                temp.append(int(k))
                k = ""
        elif flag == False and string != comma:
            temp.append(int(k))
            k = ""
            bp.append(temp)
            temp = []
    bp.sort(key = lambda x:len(x))
                
            
    return answer

solution("{{20,111},{111}}")