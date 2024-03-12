def solution(nums):
    answer = 0
    getMon = len(nums)//2
    variables = list(set(nums))
    variables = len(variables)
    if variables >= getMon:
        return getMon
    else:
        return variables
    return answer