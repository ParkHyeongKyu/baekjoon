from collections import defaultdict


def solution(genres, plays):
    answer = []

    d_cnt = defaultdict(int)
    d_play = defaultdict(list)

    for i in range(len(genres)):
        d_cnt[genres[i]] += plays[i]
        d_play[genres[i]].append((i, plays[i]))

    sorted_d_cnt_list = sorted(d_cnt.items(), key=lambda x: x[1], reverse=True)
    for genre, cnt in sorted_d_cnt_list:
        d_play[genre].sort(key=lambda x: x[1], reverse=True)
        if len(d_play[genre]) >= 2:
            for i in range(2):
                answer.append(d_play[genre][i][0])
        elif len(d_play[genre]) == 1:
            answer.append(d_play[genre][0][0])
        else:
            pass

    return answer