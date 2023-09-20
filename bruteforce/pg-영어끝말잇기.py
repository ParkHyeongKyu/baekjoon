def solution(n, words):
    answer = []
    word_set = set()

    bumin = -1

    for i in range(len(words)):
        if words[i] in word_set:
            bumin = i
            break
        elif i != 0 and words[i][0] != words[i - 1][-1]:
            bumin = i
            break
        else:
            word_set.add(words[i])

    if bumin == -1:
        answer.append(0)
        answer.append(0)
    else:
        answer.append((i % n) + 1)
        answer.append(bumin // n + 1)
    return answer