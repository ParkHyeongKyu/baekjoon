def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def is_partition_between(place, x1, y1, x2, y2):
    if x1 == x2:
        for y in range(min(y1, y2) + 1, max(y1, y2)):
            if place[x1][y] == 'X':
                return True
    elif y1 == y2:
        for x in range(min(x1, x2) + 1, max(x1, x2)):
            if place[x][y1] == 'X':
                return True
    else:  # 대각선 위치의 'P'를 위한 처리
        if place[x1][y2] == 'X' and place[x2][y1] == 'X':
            return True
    return False

def solution(places):
    answer = []

    for place in places:
        people = [(i, j) for i in range(5) for j in range(5) if place[i][j] == 'P']
        distance_rule_violated = False

        for i in range(len(people)):
            for j in range(i+1, len(people)):
                person1, person2 = people[i], people[j]
                distance = manhattan_distance(person1[0], person1[1], person2[0], person2[1])

                if distance <= 2:
                    if not is_partition_between(place, person1[0], person1[1], person2[0], person2[1]):
                        distance_rule_violated = True
                        break
            if distance_rule_violated:
                break

        answer.append(0 if distance_rule_violated else 1)

    return answer
