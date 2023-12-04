#[?] 원본 데이터 중에서 대상 데이터와 가장 가까운 값
# 순위 알고리즘: 점수 데이터에 대한 순위(등수) 구하기

import sys

def main():
    #Initialize
    #Input
    scores = [ 90, 87, 100, 95, 80]
    N = len(scores)
    rankings = [1] * 5 # 모두 1로 초기화

    #Process
    for i in range(N):
        rankings[i] = 1 # 1등으로 초기화, 순위 배열을 매 회전마다 1등으로 초기화
        for j in range(N):
            if scores[i] < scores[j]:
                rankings[i] += 1 # 나보다 큰 점수가 나오면 순위 1증가

    #Output
    for i in range(N):
        print(f"{scores[i]:3}점: {rankings[i]}등")

if __name__ == "__main__":
    main()