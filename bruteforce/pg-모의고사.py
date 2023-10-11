def solution(answers):
    answer = []
    cnt = []
    supo = []
    supo_1 = [1, 2, 3, 4, 5]  # 5
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10
    supo.append(supo_1)
    supo.append(supo_2)
    supo.append(supo_3)

    for i in range(3):
        answer_cnt = 0
        for j in range(len(answers)):
            if answers[j] == supo[i][j % len(supo[i])]:
                answer_cnt += 1
        cnt.append(answer_cnt)

    max = 0
    for i in range(3):
        if max < cnt[i]:
            max = cnt[i]
            answer = []
            answer.append(i + 1)
        elif max == cnt[i]:
            answer.append(i + 1)

    return answer