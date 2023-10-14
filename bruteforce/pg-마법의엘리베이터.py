def solution(storey):
    answer = 0
    now = storey
    while now != 0:
        if now % 10 == 0:
            temp = now
            zero_cnt = 0
            while temp % 10 == 0:
                temp /= 10
                zero_cnt += 1
            if temp % 10 <= 5:
                answer += (temp % 10)
                now -= (temp % 10) * (10 ** zero_cnt)
            else:
                answer += 10 - (temp % 10)
                now += (10 - (temp % 10)) * (10 ** zero_cnt)
        else:
            if now % 10 < 5:
                answer += now % 10
                now -= now % 10
            elif now % 10 == 5:
                temp = now - 5
                while temp % 10 == 0:
                    temp /= 10
                if temp % 10 <= 4:
                    answer += now % 10
                    now -= now % 10
                else:
                    answer += now % 10
                    now += now % 10
            else:
                answer += 10 - (now % 10)
                now += (10 - (now % 10))

    return answer