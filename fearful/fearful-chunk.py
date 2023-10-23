# 문제
# 다음과 같은 chunk 함수를 구현하시오.
#
# chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
# chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
# chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]

# 이게 iterating 방법, 시간복잡도 O(n/size)
# def chunk(arr, size):
#     chunk_num = 0
#     if len(arr) % size != 0:
#         chunk_num = len(arr) // size + 1
#     else:
#         chunk_num = len(arr) // size
#
#     result = []
#     for i in range(chunk_num):
#         if i != chunk_num-1:
#             result.append(arr[:size])
#             arr = arr[size:]
#         else:
#             result.append(arr)
#             arr = []
#
#     print(result)

# recursive 방법
def chunk(arr, size):
    if len(arr) <= size:
        return str(arr)
    else:
        chk = arr[:size]
        arr = arr[size:]
        return str(chk) + ',' + chunk(arr, size)

print(chunk([1, 2, 3, 4, 5, 6, 7, 8], 3))
