def solution(elements):
    # 원형 수열의 길이
    n = len(elements)
    # 원형 수열을 두 배로 연장
    extended_elements = elements * 2
    # 연속 부분 수열의 합을 저장할 집합
    sums_set = set()
    
    # 가능한 모든 연속 부분 수열의 합을 계산
    for start in range(n):
        current_sum = 0
        for length in range(1, n + 1):
            current_sum += extended_elements[start + length - 1]
            sums_set.add(current_sum)
    
    # 연속 부분 수열의 합으로 만들 수 있는 수의 개수 반환
    return len(sums_set)

# 예제 실행
print(solution([7, 9, 1, 1, 4]))
