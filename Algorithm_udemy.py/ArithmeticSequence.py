#[?] 1부터 20까지의 정수 중 홀수의 합을 구하는 프로그램

# 등차수열: 연속하는 두 수의 차이가 일정한 수열

#Input
sum = 0

# Process
for i in range(1, 20):
    if i % 2 == 1:
        sum += i
        if i != 19:
            print(i, end=', ')
        else:
            print(i)

#output
print(f"\n1부터 20까지의 홀수의 합: {sum}")