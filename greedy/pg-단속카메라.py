# 이차원 배열 어떤 key를 기준으로 sort하는 법 익힘
# greedy algorithm -> 진출 지점 기준으로 생각하기.

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    camera = -30001 # -30001부터 카메라 위치를 찾습니다.

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer