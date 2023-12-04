#[?] 무작위 데이터를 순서대로 ASC | DESC 정렬
# 정렬 알고리즘: 가장 [작은 | 큰] 데이터를 왼쪽으로 순서대로 이동
import sys

def main():
    #Input Data Structure(Arry, List, Stack, Tree, DB, ...)
    data = [3, 2, 1, 5, 4]
    N = len(data) # 의사코드 형대로 알고리즘을 표현하기 위함

    #Process: 선택정렬 알고리즘
    for i in range(N-1):
        for j in range(i+1, N):
            if data[i] > data[j]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
    #Output
    for i in range(N):
        print(data[i])

if __name__ == "__main__":
    main()