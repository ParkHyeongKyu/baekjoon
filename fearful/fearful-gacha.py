# 문제
# 현대 모바일 게임에서 랜덤박스 시스템은 애증의 존재이다.
# 하지만 개발자로 일하고 있다면, 랜덤박스 시스템의 선호 여부와는 관계없이 이를 만들어야 할 수도 있다.
# 1-a.
# 서버팀에서 일하는 어피치는 랜덤박스 시스템을 만들기 위해 다음 함수를 짜려고 한다.
#
# function getRandomIndexWithWeight(weightList) {
#   ...
# }
#
# 어피치를 도와서 다음 함수를 완성시켜보자. (weight 는 모두 정수이다)
# 예를 들어 [10, 20, 30, 40] 과 같은 input 이 들어왔다면, 각 인덱스(0, 1, 2, 3)가 뽑힐 확률은 10%, 20%, 30%, 40% 이다.
# [10, 10] 과 같은 input 이 들어왔다면, 각 인덱스(0, 1)가 뽑힐 확률은 50%, 50% 이다.
# 인터넷 검색을 통해 랜덤함수 사용법에 대한 정보를 얻어도 무방하다
# 1-b.
# 어피치가 만든 랜덤박스 시스템으로 가챠를 즐기는 유저들은 환호했다!(?)
# 유저들의 반응을 더 끌어올리기 위해, 우리 회사에서는 중복이 나오지 않는 랜덤박스 시스템을 만들려고 한다.
# 이번엔 중복으로 나오지 않으면서, M개 중 N개를 뽑는 함수를 완성시켜보자. getRandomIndexWithWeight 를 활용하여도 된다.
#
# function getRandomDistinctIndicesWithWeight(weightList, pickCount) {
#   ...
# }
import random


def getRandomIndexWithWeight(weightList):
    total_weight = sum(weightList)
    # 0이상 1미만 random수
    random_num = random.random()

    sum_weight = 0
    for idx, weight in enumerate(weightList):
        sum_weight += weight/total_weight
        if sum_weight >= random_num:
            return idx
    return None


def getRandomDistinctIndicesWithWeight(weightList, pickCount):
    result = []
    current_weights = weightList.copy()  # 원본 리스트를 변경하지 않기 위해 복사본을 사용합니다.

    for _ in range(pickCount):
        idx = getRandomIndexWithWeight(current_weights)
        if idx is None:
            break  # 모든 원소가 추출되었거나, 더 이상 유효한 인덱스가 없을 경우 루프를 종료합니다.
        result.append(idx)
        current_weights[idx] = 0  # 이미 선택된 항목의 가중치를 0으로 설정하여 다시 선택되지 않게 합니다.

    return result

weights = [10, 20, 30, 40]
pickCount = 2
indices = getRandomDistinctIndicesWithWeight(weights, pickCount)
print(f"Selected indices: {indices}")