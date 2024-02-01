def solution2(s, skip, index):
    answer = ""
    # a = 97, z = 122
    for word in s:
        count = 0
        bump = ord(word)
        while count < index:
            bump += 1
            if bump > 122:
                bump = 97
            if chr(bump) not in skip:
                count += 1
        answer += chr(bump)

    return answer