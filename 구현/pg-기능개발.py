import math


def solution(progresses, speeds):
    answer = []
    finish_date = []

    for i in range(len(progresses)):
        date = math.ceil((100 - progresses[i]) / speeds[i])
        finish_date.append(date)

    pin = finish_date[0]
    cnt = 1
    for i in range(1, len(finish_date)):
        if finish_date[i] <= pin:
            cnt += 1
        if finish_date[i] > pin:
            answer.append(cnt)
            pin = finish_date[i]
            cnt = 1
    answer.append(cnt)
    return answer