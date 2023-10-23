# 문제
# 우리 회사에서는 팀별로 매달 회식비를 요청한다.
# 우리 회사 공동대표 K 는 미리 정해진 회식비 예산을 아래와 같은 규칙을 이용하여 팀별로 배정하려고 한다.
#
# 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
# 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 요청에는 모두 상한액을 배정한다. 상한액 이하의 요청에 대해서는 요청한 금액을 그대로 배정한다.
#
# 예를 들어 회식비 예산이 400 이고, 3개의 팀의 회식비 요청이 100, 160, 170 인 경우 상한액을 150으로 잡으면 각각의 요청에 대해 100, 150, 150 을 배정하면 최대가 된다.
# 여러 팀의 회식비 요청과 회식비 예산의 총액이 있을 때, 위의 조건을 이용하여, 예산을 넘지 않는 회식비 상한액을 구하는 프로그램을 시간 복잡도를 고려하여 작성하시오.

budget = int(input())
team_num = int(input())
team_req = list(map(int, input().split()))

start = min(team_req)
end = max(team_req)
answer = 0

while start <= end:
    mid = (start + end) // 2
    temp_req = [0 for _ in range(team_num)]
    for i in range(team_num):
        if team_req[i] > mid:
            temp_req[i] = mid
        else:
            temp_req[i] = team_req[i]
    sum_req = sum(temp_req)

    if sum_req > budget:
        end = mid - 1
    else:
        if mid > answer:
            answer = mid
        start = mid + 1

print(answer)
