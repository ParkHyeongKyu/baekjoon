from heapq import heappush, heappop


def solution(jobs):
    sum_time = 0
    prev_now, now = -1, 0
    check_job = 0
    heap = []

    while check_job < len(jobs) or heap:
        for i in range(len(jobs)):
            if prev_now < jobs[i][0] <= now:
                heappush(heap, (jobs[i][1], jobs[i][0]))
                check_job += 1
        if heap:
            duration, start_time = heappop(heap)
            prev_now = now
            now += duration
            sum_time += now - start_time
        else:
            now += 1
    return sum_time // len(jobs)