def solution(friends, gifts):
    gifts_sent = {friend: 0 for friend in friends}
    gifts_received = {friend: 0 for friend in friends}
    next_month_gifts = {friend: 0 for friend in friends}

    for gift in gifts:
        giver, receiver = gift.split()
        gifts_sent[giver] += 1
        gifts_received[receiver] += 1

    for giver, receiver in gifts:
        balance_giver = gifts_sent[giver] - gifts_received[giver]
        balance_receiver = gifts_sent[receiver] - gifts_received[receiver]
        if balance_giver > balance_receiver:
            next_month_gifts[receiver] += 1
        elif balance_giver < balance_receiver:
            next_month_gifts[giver] += 1

    return max(next_month_gifts.values())
