def solution(participant, completion):
    answer = ''
    participant = sorted(participant)
    completion = sorted(completion)
    p_dict = {}
    c_dict = {}
    for idx, par in enumerate(participant):
        p_dict[idx] = par
    for idx, com in enumerate(completion):
        c_dict[idx] = com
    c_dict[len(completion)] = ''
    
    for i in range(len(participant)):
        if p_dict[i] != c_dict[i]:
            return p_dict[i]