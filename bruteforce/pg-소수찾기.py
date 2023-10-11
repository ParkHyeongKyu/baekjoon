from itertools import permutations


def isPrime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0
    combi_set = set()

    for i in range(1, len(numbers) + 1):
        combi_list = list(permutations(numbers, i))
        for j in range(len(combi_list)):
            combi_set.add(int(''.join(combi_list[j])))
    for combi in combi_set:
        if isPrime(combi):
            answer += 1

    return answer