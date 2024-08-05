def solution(balls, share):
    answer = 0
    temp1 = 1
    temp2 = 1
    temp3 = 1
    for b in range(balls):
        temp1 = temp1*(b+1)
    
    for s in range(share):
        temp2 = temp2*(s+1)
    for k in range(balls - share):
        temp3 = temp3*(k+1)
        
    answer = temp1//(temp2*temp3)
    return answer