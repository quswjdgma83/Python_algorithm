#최대값 알고리즘
import sys 

def main():
    #Initialize
    max = -sys.maxsize -1; # 숫자 형식의 데이터 중 가장 작은 값으로 초기화
    print(max)
    #Input
    numbers = [-2, -5, -3, -7, -1]
    N = len(numbers)
    #Process
    for i in range(0, N):
        if numbers[i] > max:
            max = numbers[i] # MAX: 더 큰값으로 할당

    #Output
    print(f"최댓값: {max}")

if __name__ == "__main__":
    main()