def solution(picks, minerals):
    answer = 0
    picks_cnt = sum(picks)
    if len(minerals) > 5 * picks_cnt:
        minerals = minerals[:5 * picks_cnt]

    if len(minerals) % 5 == 0:
        new_mineral = [[0, 0, 0] for _ in range(len(minerals) // 5)]
    else:
        new_mineral = [[0, 0, 0] for _ in range(len(minerals) // 5 + 1)]

    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            new_mineral[i // 5][0] += 1
        elif minerals[i] == "iron":
            new_mineral[i // 5][1] += 1
        else:
            new_mineral[i // 5][2] += 1

    new_mineral.sort(key=lambda x: (-x[0], -x[1], -x[2]))

    for i in range(len(new_mineral)):
        if picks[0] != 0:
            answer += sum(new_mineral[i])
            picks[0] -= 1
        elif picks[1] != 0:
            answer += 5 * new_mineral[i][0] + new_mineral[i][1] + new_mineral[i][2]
            picks[1] -= 1
        elif picks[2] != 0:
            answer += 25 * new_mineral[i][0] + 5 * new_mineral[i][1] + new_mineral[i][2]
            picks[2] -= 1
        else:
            break
    return answer