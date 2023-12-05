#주어진 범위에 주어진 조건에 해당하는 자료들의 개수
# 1부터 1000까지의 정수 중 13의 배수의 개수 (건수, 횟수)

#Input
count = 0
#Process
for i in range(1, 1000):
    if i % 13 == 0:
        count += 1

#Output
print(f"1부터 1,000 까지의 정수 중 13의 배수의 개수: {count}")