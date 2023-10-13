# n^2이라 시간초과
def solution(cap, n, deliveries, pickups):
    answer = 0

    def breakChecker():
        for i in deliveries:
            if i != 0:
                return False
        for i in pickups:
            if i != 0:
                return False
        return True

    while True:
        if breakChecker():
            break
        sum_delivery = 0
        max_distance = 0
        for i in range(len(deliveries) - 1, -1, -1):
            if sum_delivery >= cap:
                break
            if deliveries[i] > 0 and sum_delivery < cap:
                # 실을 수 있는 양
                if max_distance < i + 1:
                    max_distance = i + 1
                now_cap = cap - sum_delivery
                if now_cap >= deliveries[i]:
                    sum_delivery += deliveries[i]
                    deliveries[i] = 0
                else:
                    sum_delivery += now_cap
                    deliveries[i] -= now_cap
        # 여기까지 배달 완료
        sum_pickup = 0
        for i in range(len(pickups) - 1, -1, -1):
            if pickups[i] > 0 and sum_pickup < cap:
                if max_distance < i + 1:
                    max_distance = i + 1
                now_cap = cap - sum_pickup
                if now_cap >= pickups[i]:
                    sum_pickup += pickups[i]
                    pickups[i] = 0
                else:
                    sum_pickup += now_cap
                    pickups[i] -= now_cap
        answer += max_distance * 2

    return answer

# 시간초과 x
def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery = 0
    pickup = 0

    for i in range(n - 1, -1, -1):
        cnt = 0
        while delivery < deliveries[i] or pickup < pickups[i]:
            delivery += cap
            pickup += cap
            cnt += 1
        delivery -= deliveries[i]
        pickup -= pickups[i]
        answer += (i + 1) * cnt * 2
    return answer