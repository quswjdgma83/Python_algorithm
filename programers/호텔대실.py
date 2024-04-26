def sol(T):
    h1, m1 = T[0].split(":")
    h2, m2 = T[1].split(":")
    h1, m1 = int(h1), int(m1)
    h2, m2 = int(h2), int(m2)
    start = h1*60+m1
    end = h2*60+m2
    temp = []
    for i in range(start, end+10):
        temp.append(i)
    return temp

def solution(book_time):
    answer = 0
    dict_a = {}
    book_time = sorted(book_time, key=lambda x:x[0])
    # print(book_time)
    for book in book_time:
        # print(sol(book))
        temp = sol(book)
        for t in temp:
            if t not in dict_a:
                dict_a[t] = 1
            else:
                dict_a[t] += 1
    # print(dict_a)
    a = dict_a.values()
    answer = max(a)
    return answer