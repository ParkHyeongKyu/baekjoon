from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    rest_weight = weight

    bridge = deque()

    q = deque(truck_weights)
    while q or bridge:
        answer += 1
        if bridge:
            for i in range(len(bridge)):
                bridge[i][0] -= 1
            if bridge[0][0] == 0:
                rest_weight = rest_weight + bridge[0][1]
                bridge.popleft()
        if q and rest_weight >= q[0] and len(bridge) < bridge_length:
            now = q.popleft()
            rest_weight = rest_weight - now
            bridge.append([bridge_length, now])
    return answer