def solution(X, Y):
    answer = ''
    x = set(str(X))
    y = set(str(Y))
    both = x.intersection(y)
    result = []
            
    for num in both:
        goal = 0
        a = X.count(num)
        b = Y.count(num)
        goal = min(a, b)
        for _ in range(goal):
            result.append(num)
            
    result_num = [ int(num) for num in result]
    if len(result) == 0:
        return "-1"
    if sum(result_num) == 0:
        return "0"
    result = sorted(result, reverse = True)
    answer = "".join(result)
    
        
    return answer