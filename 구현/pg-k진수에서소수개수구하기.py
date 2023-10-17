def isPrime(n):
    if 1 < n < 4:
        return True
    elif n <= 1:
        return False

    for i in range(2, int((n ** 0.5)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    new_number = ''

    while n != 0:
        new_number = str(n % k) + new_number
        n = n // k

    start_idx = 0
    end_idx = -1
    for i in range(len(new_number)):
        if new_number[i] != '0' and i > 0 and new_number[i - 1] == '0':
            start_idx = i
            end_idx = i
        elif new_number[i] != '0' and i > 0 and new_number[i - 1] != '0':
            end_idx += 1
        elif new_number[i] != '0' and i == 0:
            end_idx += 1
        # start_idx ~ end_idx 가 소수인지 판별
        else:
            if isPrime(int(new_number[start_idx:end_idx + 1])):
                # case1
                if start_idx - 1 >= 0 and new_number[start_idx - 1] == '0' and end_idx + 1 < len(new_number) and \
                        new_number[end_idx + 1] == '0':
                    answer += 1
                # case2
                elif start_idx == 0 and end_idx + 1 < len(new_number) and new_number[end_idx + 1] == '0':
                    answer += 1
                elif start_idx - 1 >= 0 and new_number[start_idx - 1] == '0' and end_idx == len(new_number) - 1:
                    answer += 1
                elif start_idx == 0 and end_idx == len(new_number) - 1:
                    answer += 1
            start_idx = end_idx + 1
            end_idx = start_idx

    if isPrime(int(new_number[start_idx:end_idx + 1])):
        # case1
        if start_idx - 1 >= 0 and new_number[start_idx - 1] == '0' and end_idx + 1 < len(new_number) and new_number[
            end_idx + 1] == '0':
            answer += 1
        # case2
        elif start_idx == 0 and end_idx + 1 < len(new_number) and new_number[end_idx + 1] == '0':
            answer += 1
        elif start_idx - 1 >= 0 and new_number[start_idx - 1] == '0' and end_idx == len(new_number) - 1:
            answer += 1
        elif start_idx == 0 and end_idx == len(new_number) - 1:
            answer += 1
    return answer