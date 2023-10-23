# 문제
# 1차원 선이 있다고 가정할 때, 시작점과 끝점이 있는 막대의 리스트가 주어진다.
# 이때, 오버랩되는 막대를 합친 결과를 출력하여라.
#
# Example 1)
#
# Input: [(1,3), (2,6), (8,10), (15,18)]
#
# Output: [(1,6), (8,10), (15,18)]
#
# // (1,3), (2,6) 이 합쳐짐
#
#
#
# Example 2)
#
# Input: [(1,4), (4,5), (5,10)]
#
# Output: [(1,10)]
#
# // (1,4), (4,5), (5,10) 가 전부 합쳐짐

# 맞는데 시간복잡도가 너무 높다... 무려 n^2logn
def integrate_bar(lst):
    while True:
        lst.sort()
        flag = True
        for i in range(len(lst)-1):
            if lst[i][1] >= lst[i+1][0]:
                start = lst[i][0]
                end = lst[i+1][1]
                lst.pop(i)
                lst.pop(i)
                lst.append((start, end))
                flag = False
                break
        if flag:
            break

    return lst

print(integrate_bar([(1,4), (4,5), (5,10)]))

# nlogn에 할 수 있는 방법은 없을까?
# flag 배열을 만들어 두고 합쳐지는 것 끼리 표시한 뒤, 마지막에 합치기 => 이러면 nlogn 가능 !