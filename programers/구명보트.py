def solution(people, limit):
    people = sorted(people, reverse=True)
    answer = 0
    s = 0
    e = len(people)-1
    count = 0
    # 경우의 수
    # 1. 혼자만 2. 혼자 + 끝, 3. 여러개
    while(people != []):
        if s == e:
            count += 1
            break
        if people[s] + people[e] > limit:
            s += 1
            count += 1
        elif people[s] + people[e] <= limit:
            s += 1
            if s == e:
                count += 1
                break
            e -= 1
            count += 1
    answer = count

    return answer

solution([70,50,80,50], 100)
# solution([70, 80, 50], 100)