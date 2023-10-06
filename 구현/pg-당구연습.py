import sys


def solution(m, n, startX, startY, balls):
    answer = []

    for i in range(len(balls)):
        dist = []
        # 왼쪽벽
        dist1, dist2, dist3, dist4 = sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize
        if not (startY == balls[i][1] and startX > balls[i][0]):
            dist1 = (balls[i][0] + startX) ** 2 + (balls[i][1] - startY) ** 2
        # 오른쪽 벽
        if not (startY == balls[i][1] and startX < balls[i][0]):
            dist2 = (2 * m - startX - balls[i][0]) ** 2 + (balls[i][1] - startY) ** 2
        # 위쪽 벽
        if not (startX == balls[i][0] and startY < balls[i][1]):
            dist3 = (2 * n - startY - balls[i][1]) ** 2 + (balls[i][0] - startX) ** 2
        # 아래쪽 벽
        if not (startX == balls[i][0] and startY > balls[i][1]):
            dist4 = (balls[i][1] + startY) ** 2 + (balls[i][0] - startX) ** 2
        answer.append(min(dist1, dist2, dist3, dist4))
    return answer