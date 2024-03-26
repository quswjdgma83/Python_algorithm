from collections import deque

def solution(cacheSize, cities):
    answer = 0
    HIT = 1
    MISS = 5
    cities = [city.lower() for city in cities]
    cache = deque([0 for _ in range(cacheSize)])
    for city in cities:
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += HIT
        else:
            cache.append(city)
            cache.popleft()
            answer += MISS
    return answer