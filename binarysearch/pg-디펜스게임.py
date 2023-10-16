def solution(n, k, enemy):
    answer = 0

    def bs(start, end):
        nonlocal n, k, enemy, answer
        while start <= end:
            mid = (start + end) // 2  # 처리 가능한 라운드의 수

            now_enemy = enemy[:mid + 1]
            now_enemy.sort()
            sum_enemy = sum(now_enemy)
            max_enemy = now_enemy[-k:]

            if sum_enemy - sum(max_enemy) <= n:
                answer = mid
                start = mid + 1
            else:
                end = mid - 1

    bs(1, len(enemy) - 1)

    return answer + 1