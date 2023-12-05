#[?] 원본 데이터 중에서 대상 데이터와 가장 가까운 값
# 근삿값 알고리즘
# 가까운 값 -> 차잇값의 절댓값의 최솟값: 근삿값의 정의
import sys

def main():
    #Initialize
    min = sys.maxsize
    #Input
    numbers = [10, 20, 30, 27, 17]
    target = 25
    neer = 0
    #Process
    for i in range(0, len(numbers)):
        if abs(target - numbers[i]) < min:
            neer = numbers[i]
            min = abs(target - numbers[i])

    #Output
    print(f"{target}와/과 가장 가까운 값: {neer}(차이: {min})")

if __name__ == "__main__":
    main()