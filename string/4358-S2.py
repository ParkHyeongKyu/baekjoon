# 문제
# 생태학에서 나무의 분포도를 측정하는 것은 중요하다. 그러므로 당신은 미국 전역의 나무들이 주어졌을 때, 각 종이 전체에서 몇 %를 차지하는지 구하는 프로그램을 만들어야 한다.

# 입력
# 프로그램은 여러 줄로 이루어져 있으며, 한 줄에 하나의 나무 종 이름이 주어진다.
# 어떤 종 이름도 30글자를 넘지 않으며, 입력에는 최대 10,000개의 종이 주어지고 최대 1,000,000그루의 나무가 주어진다.

# 츌력
# 주어진 각 종의 이름을 사전순으로 출력하고, 그 종이 차지하는 비율을 백분율로 소수점 4째자리까지 반올림해 함께 출력한다.

from collections import defaultdict
import sys

trees = defaultdict(int)
float_trees = defaultdict(float)
all_tree_count = 0

while True:
    tree = sys.stdin.readline().rstrip()
    if tree == '':
        break

    trees[tree] += 1
    all_tree_count += 1

for tree in trees.keys():
    # float_trees[tree] = round(trees[tree] / all_tree_count * 100, 4)
    float_trees[tree] = trees[tree] / all_tree_count * 100

for item in sorted(float_trees.keys()):
    # print(f'{item} {float_trees[item]}')
    print("%s %.4f" %(item, float_trees[item]))

# 처음엔 round를 이용하여 반올림을 하려고 하였지만 틀렸다고 나옴. round의 float에 대한 반올림은 정확하지 않을 수 있다고 함.
# float에 대한 round() 의 동작은 예상과 다를 수 있습니다: 예 들어, round(2.675, 2) 는 2.68 대신에 2.67 을 제공합니다.
# 이것은 버그가 아닙니다: 대부분의 십진 소수가 float로 정확히 표현될 수 없다는 사실로부터 오는 결과입니다.
