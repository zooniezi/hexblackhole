from collections import deque

# 보드판 출력 함수
def print_board(board):
    # 글씨 색상 설정을 위한 함수
    def colored_text(value, color_code):
        return f"\033[{color_code}m{value}\033[0m"

    # board[i][1]에 따라 색상 변경 (빨간색은 91, 파란색은 94)
    def get_colored_value(i):
        if board[i][1] == 1:
            return colored_text(board[i][0], 91)  # 빨간색(흑)
        elif board[i][1] == 2:
            return colored_text(board[i][0], 94)  # 파란색(백)
        else:
            return colored_text(board[i][0], 93) #노란색(빈칸)

    # 출력 부분
    print(f"    {get_colored_value(1)}   {get_colored_value(2)}   {get_colored_value(3)}")
    print(f"  {get_colored_value(4)}   {get_colored_value(5)}   {get_colored_value(6)}   {get_colored_value(7)}")
    print(f"{get_colored_value(8)}   {get_colored_value(9)}   {get_colored_value(10)}   {get_colored_value(11)}   {get_colored_value(12)}")
    print(f"  {get_colored_value(13)}   {get_colored_value(14)}   {get_colored_value(15)}   {get_colored_value(16)}")
    print(f"    {get_colored_value(17)}   {get_colored_value(18)}   {get_colored_value(19)}")
    return

# 게임 종료 조건 확인 함수
def game_over(board):
    """
    Check that the game has ended

    Args:
        board (list): gameboard which contains each card number in space
    
    Returns:
        bool: Whether the game has ended
    """
    count_empty_space = 0
    for i in range(1,len(board)):
        if board[i][1] == 0:
            count_empty_space += 1
    if count_empty_space == 1:
        return True
    return False

def blackhole_swallow(board,adjacent):
    """
    After game ends, remove blackhole and all adjacent spaces.

    Args:
        board (list): gameboard which contains each card number in space
        adjacent (list): adjacency graph
    
    Returns:
        none
    """
    # 블랙홀 위치 확인하기
    blackhole = 0
    for i in range(1,len(board)):
        if board[i][1] == 0:
            blackhole = i
            break
    # 블랙홀 주위는 빈칸으로 만들기
    for adjacent_with_blackhole in adjacent[blackhole]:
        board[adjacent_with_blackhole] = [0,0]

def check_score(board,adjacent,player_num):
    score = 0
    visited = [False for i in range(20)]
    for now_space in range(1,20):
        if board[now_space][1] == player_num and not visited[now_space]:
            now_cluster = deque([[now_space,board[now_space][0]]])
            visited[now_space] = True
            length_of_cluster = 0
            
            while now_cluster:
                node = now_cluster.popleft()
                node_space = node[0]
                length_of_cluster+=1

                for adjacent_space in adjacent[node_space]:
                    if board[adjacent_space][1] == player_num and not visited[adjacent_space]:
                        now_cluster.append([adjacent_space,board[adjacent_space][0]])
                        visited[adjacent_space] = True

            if length_of_cluster == 1:
                score+=board[now_space][0]
            else:
                score+=length_of_cluster
    return score


def who_place_first(p1card,p2card,tiebreaker):
    if p1card[0] < p2card[0]:
        return [p1card,p2card]
    
    if p1card[0] > p2card[0]:
        return [p2card,p1card]
    
    if p1card[0] == p2card[0]:
        if p1card[1] == tiebreaker:
            return [p1card,p2card]
        else:
            return [p2card,p1card]