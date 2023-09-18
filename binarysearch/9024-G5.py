# 문제
# 여러 개의 서로 다른 정수 S = {a1, a2, …, an} 와 또 다른 정수 K 가 주어졌을 때, S 에 속하는 서로 다른 두 개의 정수의 합이 K 에 가장 가까운 두 정수를 구하시오.
# 예를 들어, 10 개의 정수
#
# S = { -7, 9, 2, -4, 12, 1, 5, -3, -2, 0}
#
# 가 주어졌을 때, K = 8 에 그 합이 가장 가까운 두 정수는 {12, -4} 이다.
# 또한 K = 4 에 그 합이 가장 가까운 두 정수는 {-7, 12}, {9, -4}, {5, -2}, {5, 0}, {1, 2} 등의 다섯 종류가 있다.
#
# 여러 개의 서로 다른 정수가 주어졌을 때, 주어진 정수들 중에서 서로 다른 두 정수의 합이 주어진 또 다른 정수에 가장 가까운 두 정수의 조합의 수를 계산하는 프로그램을 작성하시오.

# 입력
# 프로그램은 표준입력으로 입력을 받는다. 프로그램 입력은 t 개의 테스트 케이스로 구성된다. 입력의 첫 번째 줄에 테스트 케이스의 개수를 나타내는 정수 t 가 주어진다.
# 두 번째 줄부터 두 줄에 한 개의 테스트 케이스에 해당하는 데이터가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 두 개의 정수 n 과 K (2 ≤ n ≤ 1,000,000, -108 ≤ K ≤ 108 )가 한 개의 공백을 사이에 두고 입력된다.
# 두 번째 줄에는 n 개의 정수가 하나의 공백을 사이에 두고 주어지며, 각 정수의 최댓값은 108 이고, 최솟값은 -108 이다. 잘못된 데이터가 입력되는 경우는 없다.

# 출력
# 출력은 표준출력(standard output)을 사용한다. 입력되는 테스트 케이스의 순서대로 다음 줄에 이어서 각 테스트 케이스의 결과를 출력한다.
# 각 테스트 케이스의 출력되는 첫 줄에 입력으로 주어진 n 개의 정수들 중에서 서로 다른 두 정수의 합이 주어진 또 다른 정수 K 에 가장 가까운 두 정수의 조합의 수를 출력한다.
import sys

test_case = int(sys.stdin.readline().rstrip())

for tc in range(test_case):
    n, k = map(int, sys.stdin.readline().rstrip().split())
    s = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

    start, end = 0, -1
    sim = sys.maxsize
    sim_cnt = 0
    while s[start] < s[end]:
        if abs((s[start] + s[end] - k)) == sim:
            sim_cnt += 1
        elif abs((s[start] + s[end] - k)) < sim:
            sim = abs((s[start] + s[end] - k))
            sim_cnt = 1

        if (s[start] + s[end]) - k <= 0:
            start += 1
        elif (s[start] + s[end]) - k > 0:
            end -= 1

    print(sim_cnt)


