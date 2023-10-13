from heapq import heappush, heappop


def solution(operations):
    min_heap = []
    max_heap = []
    for operation in operations:
        op, value = operation.split()
        value = int(value)
        if op == 'I':
            heappush(min_heap, value)
            heappush(max_heap, -value)  # Max heap 구현을 위해 음수로 저장
        elif value == 1 and max_heap:  # 최댓값 삭제
            max_val = heappop(max_heap)
            min_heap.remove(-max_val)  # 최댓값을 최소 힙에서도 삭제
        elif value == -1 and min_heap:  # 최솟값 삭제
            min_val = heappop(min_heap)
            max_heap.remove(-min_val)  # 최솟값을 최대 힙에서도 삭제

    # 동기화: min_heap과 max_heap 간의 동기를 맞춰주는 작업이 필요할 수 있습니다.
    # 이는 요구사항과 데이터의 특성에 따라 달라질 수 있습니다.

    if not min_heap:  # 빈 힙 처리
        return [0, 0]
    else:
        return [-heappop(max_heap), heappop(min_heap)]  # 최댓값, 최솟값 반환