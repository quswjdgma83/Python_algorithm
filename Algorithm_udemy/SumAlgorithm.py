# Input: n명의 점수

scores = [100, 75, 50, 37, 90, 95]
sum = 0
N = len(scores)

# Process 합계 알고리즘 영역
for i in range (N):
    if scores[i] >= 80:
        sum += scores[i]


# Output 출력
print(f"{N}명의 점수 중 80점 이상의 총점 {sum}")