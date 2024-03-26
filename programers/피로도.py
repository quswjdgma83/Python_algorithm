def solution(k, dungeons):
    answer = -1  # 탐색을 통해 찾을 최대 던전 탐험 수를 저장할 변수, 초기값은 -1로 설정

    def bt(c, k, ds):
        nonlocal answer  # 외부 함수의 변수를 내부 함수에서 사용하기 위해 nonlocal 키워드 사용

        for i, d in enumerate(ds):  # 현재 탐색 가능한 모든 던전에 대해 반복
            if k >= d[0]:  # 만약 현재 피로도가 던전 탐험의 최소 필요 피로도 이상이라면
                new_dungeons = ds.copy()  # 현재 던전 리스트 복사
                new_dungeons.pop(i)  # 탐험한 던전 제거

                # 재귀적으로 다음 던전 탐험 시도, c + 1은 현재까지 탐험한 던전 수, k - d[1]은 남은 피로도
                clear = bt(c + 1, k - d[1], new_dungeons)

                if answer < clear:  # 만약 현재까지 찾은 최대 탐험 수보다 더 많은 던전을 탐험할 수 있다면
                    answer = clear  # 최대 탐험 가능 던전 수 갱신
        return c  # 현재까지 탐험한 던전 수 반환

    bt(0, k, dungeons)  # 백트래킹 시작

    return answer  # 최대 탐험 가능 던전 수 반환


solution(80,[[80,20],[50,40],[30,10]])