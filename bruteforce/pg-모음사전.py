from itertools import permutations

words = ['A', 'E', 'I', 'O', 'U']


def makeWords_1():
    global words
    result = []
    for i in words:
        result.append(i)

    return result


def makeWords_2():
    global words
    result = []
    for i in words:
        for j in words:
            result.append(i + j)
    return result


def makeWords_3():
    global words
    result = []
    for i in words:
        for j in words:
            for k in words:
                result.append(i + j + k)
    return result


def makeWords_4():
    global words
    result = []
    for i in words:
        for j in words:
            for k in words:
                for t in words:
                    result.append(i + j + k + t)
    return result


def makeWords_5():
    global words
    result = []
    for i in words:
        for j in words:
            for k in words:
                for t in words:
                    for p in words:
                        result.append(i + j + k + t + p)
    return result


def solution(word):
    answer = 0
    all_words = []
    all_words.extend(makeWords_1())
    all_words.extend(makeWords_2())
    all_words.extend(makeWords_3())
    all_words.extend(makeWords_4())
    all_words.extend(makeWords_5())
    all_words.sort()

    return all_words.index(word) + 1

# itertools product를 사용한 예시

from itertools import product


def solution(word):
    answer = 0
    worda = ['A', 'E', 'I', 'O', 'U']
    all_words = []

    for i in range(1, 6):
        word_list = list(product(worda, repeat=i))
        for j in range(len(word_list)):
            all_words.append(''.join(word_list[j]))

    all_words.sort()
    return all_words.index(word) + 1