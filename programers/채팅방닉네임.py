def solution(record):
    answer = []
    userInfo = {}
    for data in record:
        low_data = data.split(" ")
        state = low_data[0]  # 상태
        userId = low_data[1]  # 유저 아이디
        if state == "Enter" or state == "Change":
            userInfo[userId] = low_data[2]
            
    for data in record:
        low_data = data.split(" ")
        state = low_data[0]  # 상태
        userId = low_data[1]  # 유저 아이디
        if state == "Enter":
            answer.append(userInfo[userId]+"님이 들어왔습니다.")
        elif state == "Leave":
            answer.append(userInfo[userId]+"님이 나갔습니다.")
    return answer
