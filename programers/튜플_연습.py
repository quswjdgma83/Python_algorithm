def solution(s):
    # '{', '}'을 기준으로 문자열을 분리하고, 빈 문자열을 제거합니다.
    sets = s[2:-2].split("},{")
    
    # 각 집합을 ','를 기준으로 분리하고, 정수 리스트로 변환한 뒤, 길이에 따라 정렬합니다.
    sorted_sets = sorted([list(map(int, set_.split(','))) for set_ in sets], key=len)
    
    print(sorted_sets)
    answer = []
    # 정렬된 각 집합에 대해 순회하면서, 결과 리스트에 없는 숫자를 찾아 추가합니다.
    for set_ in sorted_sets:
        for num in set_:
            if num not in answer:
                answer.append(num)
                break  # 중복되지 않는 첫 번째 숫자만 추가하면 됩니다.
    
    return answer

# # 테스트
# print(solution("{{20,111},{111}}"))


solution("{{20,111},{111}}")