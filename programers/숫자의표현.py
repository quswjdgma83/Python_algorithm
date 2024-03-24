def solution(n):
    answer = 0
    start, end = 1, 1  # 두 포인터 초기화
    sum_nums = 1  # 초기 합은 첫 번째 숫자인 1

    while start <= n // 2:  # start가 n의 절반을 넘어서면 검사할 필요가 없음
        if sum_nums < n:
            # 합이 n보다 작으면 끝 인덱스를 증가시키고 해당 값을 합에 더함
            end += 1
            sum_nums += end
        elif sum_nums > n:
            # 합이 n보다 크면 시작 값을 합에서 빼고 시작 인덱스를 증가시킴
            sum_nums -= start
            start += 1
        else:
            # 합이 n과 같으면 정답 카운트를 증가시키고 시작 값을 합에서 빼고 시작 인덱스를 증가시킴
            answer += 1
            sum_nums -= start
            start += 1
    
    return answer + 1  # 자기 자신도 포함되므로 +1