def solution(distance, rocks, n):
    answer = 0

    start = 1
    end = distance

    rocks.append(distance)
    rocks.sort()

    while start <= end:
        mid = (start + end) // 2

        prev_rock = 0
        del_rock_cnt = 0
        for rock in rocks:
            dist = rock - prev_rock
            if dist < mid:
                del_rock_cnt += 1
                if del_rock_cnt > n:
                    break
            else:
                prev_rock = rock

        if del_rock_cnt > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer