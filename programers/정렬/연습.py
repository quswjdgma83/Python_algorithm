# 예시 데이터
count = [10, 5, 8, 3]  # 인덱스 0, 1, 2, 3의 값들이 존재
order2 = [(1, 100, 3), (0, 50, 5), (2, 70, 2), (3, 90, 4)]

# count의 값을 기준으로 정렬
sorted_order = sorted(order2, key=lambda x: count[x[0]])

# 결과 출력
print(sorted_order)