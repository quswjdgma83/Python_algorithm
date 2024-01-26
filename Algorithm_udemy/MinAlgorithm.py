#최솟값 알고리즘: 주어진 범위 + 주어진 조건의 자료들의 가장 작은 값
import sys

def main():
    #Initialize
    min = sys.maxsize

    #Input
    numbers = [2, 5, 3, 7, 1]

    #Process
    for number in numbers:
        if number < min and number % 2 == 0:
            min = number

    #Output
    print(f"짝수 최솟값: {min}")

if __name__ == "__main__":
    main()