realResult = {}

def makeTermDict(terms):
    for term in terms:
        a, b = term.split(" ")
        realResult[a] = int(b)
    return
# 1달: 28일
# 1년: 280+56 = 336일de
def calcDetailDay(days, plus):#더하기 연산
     a = 0
     y, m, d = days.split(".")
     a += 336*int(y) + 28*int(m) + int(d) + int(plus)*28
     return a

def makeDay(privacies, today):
        result = []
        count = 0
        for privacy in privacies:
            count += 1
            day, key = privacy.split(" ")
            print("오늘",today,todayCalc(today))
            print("개정일", privacy,calcDetailDay(day, realResult[key]))
            if todayCalc(today)-1 > calcDetailDay(day, realResult[key]):
                 result.append(count)

        return result

def todayCalc(today):
     a = 0
     y, m, d = today.split(".")
     a += 336*int(y) + 28*int(m) + int(d)
     return a

def solution(today, terms, privacies):
    answer = []
    makeTermDict(terms)
    answer = makeDay(privacies, today)
    print(answer)
    return answer

solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])
