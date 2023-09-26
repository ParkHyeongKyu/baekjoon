def datetime_minus(time1, time2):
    hour = int(time1[0:2])
    minute = int(time1[3:])
    hour2 = int(time2[0:2])
    minute2 = int(time2[3:])
    diff = int((hour * 60 + minute)) - int((hour2 * 60 + minute2))
    return diff


def solution(plans):
    answer = []
    plans.sort(key=lambda x: x[1])

    diffs = []
    stack = []
    for i in range(1, len(plans)):
        diffs.append(datetime_minus(plans[i][1], plans[i - 1][1]))

    for i in range(len(diffs)):
        if diffs[i] >= int(plans[i][2]):
            answer.append(plans[i][0])
            remain_time = int(diffs[i]) - int(plans[i][2])
            while stack:
                recent = stack.pop()
                if recent[1] <= remain_time:
                    remain_time = remain_time - int(recent[1])
                    answer.append(recent[0])
                else:
                    stack.append((recent[0], int(recent[1]) - remain_time))
                    break
        else:
            stack.append((plans[i][0], int(plans[i][2]) - diffs[i]))

    stack.append((plans[-1][0], plans[-1][2]))

    while stack:
        now = stack.pop()
        answer.append(now[0])

    return answer

# music 30, computer 90,
# science -> 13:30
# music 30, computer 60
# history -> 14:30
# computer
# music