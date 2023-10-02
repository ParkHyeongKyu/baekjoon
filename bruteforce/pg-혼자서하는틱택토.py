# 안되는 경우
# 1. X가 O보다 많은 경우
# 2. O가 이미 3칸인데 X가 동일한 개수일 때
# 3. X가 이미 3칸인데 O가 더 많을 때
# 4. O와 X의 개수 차이가 1개보다 많을 때

def check(board, mark):
    if board[0][0] == board[0][1] == board[0][2] == mark:
        return True
    elif board[1][0] == board[1][1] == board[1][2] == mark:
        return True
    elif board[2][0] == board[2][1] == board[2][2] == mark:
        return True
    elif board[0][0] == board[1][0] == board[2][0] == mark:
        return True
    elif board[0][1] == board[1][1] == board[2][1] == mark:
        return True
    elif board[0][2] == board[1][2] == board[2][2] == mark:
        return True
    elif board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    else:
        return False


def solution(board):
    answer = -1
    x_cnt, o_cnt = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                o_cnt += 1
            elif board[i][j] == 'X':
                x_cnt += 1

    if abs(o_cnt - x_cnt) > 1 or x_cnt > o_cnt:
        answer = 0
    elif check(board, 'O') and x_cnt == o_cnt:
        answer = 0
    elif check(board, 'X') and o_cnt > x_cnt:
        answer = 0
    else:
        answer = 1
    return answer