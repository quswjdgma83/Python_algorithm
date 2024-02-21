def solution(players, callings):
    rank={}
    for i, player in enumerate(players):
        rank[player] = i

    for call in callings:
        callIdx = rank[call]

        prevIdx = callIdx-1
        prevPlayer = players[prevIdx]
        players[callIdx], players[prevIdx] = players[prevIdx], players[callIdx]
        rank[call], rank[prevPlayer] = rank[prevPlayer], rank[call]
        print(players)
    return players

solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])