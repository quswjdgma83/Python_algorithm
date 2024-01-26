#[?] n명의 점수 중에서 80점 이상 95점 이하인 점수의 평균

#Input
datas = [90, 65, 78, 50, 95]
sum = 0
count = 0
#Process
for data in datas:
    if 80 <= data <= 95:
        sum += data
        count += 1

#Output
print(f"정답: {sum/count:.2f}")