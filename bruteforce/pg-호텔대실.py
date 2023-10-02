from datetime import datetime, timedelta

def solution(book_time):
    # 종료 시간에 청소 시간을 더하고, 종료 시간을 기준으로 정렬
    book_time = [(datetime.strptime(start, "%H:%M"), datetime.strptime(end, "%H:%M") + timedelta(minutes=10)) for start, end in book_time]
    book_time.sort(key=lambda x: x[0])  # 시작 시간을 기준으로 정렬

    rooms = []  # 각 방의 다음 사용 가능 시간을 저장

    for start, end in book_time:
        assigned = False
        for i in range(len(rooms)):
            if rooms[i] <= start:
                rooms[i] = end
                assigned = True
                break
        if not assigned:
            rooms.append(end)

    return len(rooms)