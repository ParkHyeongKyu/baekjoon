def solution(citations):
    answer = 0

    citations.sort()
    start = 0
    end = max(citations)
    while start <= end:
        mid = (start + end) // 2
        cnt_high, cnt_low = 0, 0
        for i in range(len(citations)):
            if citations[i] >= mid:
                cnt_high += 1
            elif citations[i] <= mid:
                cnt_low += 1

        if cnt_high < mid:
            end = mid - 1
        elif cnt_high >= mid:
            answer = mid
            start = mid + 1
    return answer