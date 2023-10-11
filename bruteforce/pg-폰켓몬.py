def solution(nums):
    choose_num = len(nums) // 2

    visited = [False for _ in range(200001)]

    cnt = 0

    for i in nums:
        if not visited[i]:
            visited[i] = True
            cnt += 1

    if cnt > choose_num:
        return choose_num
    else:
        return cnt