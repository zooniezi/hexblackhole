from random import shuffle
from collections import deque


class Game:
    def __init__(self, player1, player2, tiebreaker, verbose=False) -> None:
        self.player1 = player1
        self.player2 = player2
        self.verbose = verbose
        # 기보관리
        # self.notation = [[[],[]] for i in range(10)]
        self.turn = 0
        self.player1_score = 0
        self.player2_score = 0
        self.board = [[i, 0] for i in range(20)]
        self.adjacent = [
            [],
            [2, 4, 5],
            [1, 3, 5, 6],
            [2, 6, 7],
            [1, 5, 8, 9],
            [1, 2, 4, 6, 9, 10],
            [2, 3, 5, 7, 10, 11],
            [3, 6, 11, 12],
            [4, 9, 13],
            [4, 5, 8, 10, 13, 14],
            [5, 6, 9, 11, 14, 15],
            [6, 7, 10, 12, 15, 16],
            [7, 11, 16],
            [8, 9, 14, 17],
            [9, 10, 13, 15, 17, 18],
            [10, 11, 14, 16, 18, 19],
            [11, 12, 15, 19],
            [13, 14, 18],
            [14, 15, 17, 19],
            [15, 16, 18],
        ]
        # 같은 숫자를 낸 경우 우선권 선언(기본:1-흑색 우선)
        self.tiebreaker = tiebreaker

        # 점수 계산에 쓰일 변수 선언
        self.black_score = 0
        self.white_score = 0

        # 각 플레이어 전체 카드풀 만들기 및 1카드는 서로 반대 색으로 설정하기
        self.black_cards = [[i, 1] for i in range(1, 12)]
        self.white_cards = [[i, 2] for i in range(1, 12)]
        self.black_cards[0][1] = 2
        self.white_cards[0][1] = 1

        # 카드 덱 섞기
        shuffle(self.black_cards)
        shuffle(self.white_cards)

        # 게임 시작 전 초기 손패 뽑기
        self.player_black_hand = [
            self.black_cards.pop(),
            self.black_cards.pop(),
            self.black_cards.pop(),
        ]
        self.player_white_hand = [
            self.white_cards.pop(),
            self.white_cards.pop(),
            self.white_cards.pop(),
        ]

    def print_board(self):
        board = self.board

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
                return colored_text(board[i][0], 93)  # 노란색(빈칸)

        # 출력 부분
        if self.verbose:
            print(
                f"    {get_colored_value(1)}   {get_colored_value(2)}   {get_colored_value(3)}"
            )
            print(
                f"  {get_colored_value(4)}   {get_colored_value(5)}   {get_colored_value(6)}   {get_colored_value(7)}"
            )
            print(
                f"{get_colored_value(8)}   {get_colored_value(9)}   {get_colored_value(10)}   {get_colored_value(11)}   {get_colored_value(12)}"
            )
            print(
                f"  {get_colored_value(13)}   {get_colored_value(14)}   {get_colored_value(15)}   {get_colored_value(16)}"
            )
            print(
                f"    {get_colored_value(17)}   {get_colored_value(18)}   {get_colored_value(19)}"
            )
        return

        # 게임 종료 조건 확인 함수

    def game_over(self):
        """
        Check that the game has ended

        Args:
            board (list): gameboard which contains each card number in space

        Returns:
            bool: Whether the game has ended
        """
        board = self.board
        count_empty_space = 0
        for i in range(1, len(board)):
            if board[i][1] == 0:
                count_empty_space += 1
        if count_empty_space == 1:
            return True
        return False

    def blackhole_swallow(self):
        """
        After game ends, remove blackhole and all adjacent spaces.

        Args:
            board (list): gameboard which contains each card number in space
            adjacent (list): adjacency graph

        Returns:
            none
        """
        board = self.board
        adjacent = self.adjacent
        # 블랙홀 위치 확인하기
        blackhole = 0
        for i in range(1, len(board)):
            if board[i][1] == 0:
                blackhole = i
                break
        # 블랙홀 주위는 빈칸으로 만들기
        for adjacent_with_blackhole in adjacent[blackhole]:
            board[adjacent_with_blackhole] = [0, 0]

    def check_score(self, player_num):

        board = self.board
        adjacent = self.adjacent

        score = 0
        visited = [False for i in range(20)]
        for now_space in range(1, 20):
            if board[now_space][1] == player_num and not visited[now_space]:
                now_cluster = deque([[now_space, board[now_space][0]]])
                visited[now_space] = True
                length_of_cluster = 0

                while now_cluster:
                    node = now_cluster.popleft()
                    node_space = node[0]
                    length_of_cluster += 1

                    for adjacent_space in adjacent[node_space]:
                        if (
                            board[adjacent_space][1] == player_num
                            and not visited[adjacent_space]
                        ):
                            now_cluster.append(
                                [adjacent_space, board[adjacent_space][0]]
                            )
                            visited[adjacent_space] = True

                if length_of_cluster == 1:
                    score += board[now_space][0]
                else:
                    score += length_of_cluster
        return score

    def who_place_first(self, p1card, p2card):
        tiebreaker = self.tiebreaker

        if p1card[0] < p2card[0]:
            return 1

        elif p1card[0] > p2card[0]:
            return 2

        else:
            if p1card[1] == tiebreaker:
                return 1
            else:
                return 2

    #숫자 6 능력 발동 관련 처리 함수
    def try_special_move(self, placed_location, color, player):
        movable = self.get_adjacent_same_color_tiles(placed_location, color)  # 6번 타일 기준 같은 색 타일들
        destinations = self.get_adjacent_empty_positions(placed_location)    # 6번 타일 기준 빈칸만!

        if self.verbose:
            print(f"[능력체크] 6번 타일 착수 위치: {placed_location}")
            print(f"[능력체크] 이동 가능한 같은 색 타일: {movable}")
            print(f"[능력체크] 이동 가능한 목적지 후보 (6번 타일 주변): {destinations}")
        
        self.print_board()

        if movable and destinations:
            move = player.choose_relocation(self.board, movable, destinations, placed_location)
            if move:
                from_pos, to_pos = move
                self.board[to_pos] = self.board[from_pos]
                self.board[from_pos] = [from_pos, 0]
                self.print_board()

    def process_turn(self):
        if self.game_over():
            self.blackhole_swallow()
            self.black_score = self.check_score(1)
            self.white_score = self.check_score(2)
            if self.black_score > self.white_score:
                # black player's color printed in red color
                winning_call = "Red wins"
            elif self.black_score < self.white_score:
                # white player's color printed in blue color
                winning_call = "Blue wins"
            else:
                winning_call = "Draw"
            if self.verbose:
                print("Result")
                self.print_board()
                print()
                print(
                    f"Total Score\nRed : {self.black_score}\nBlue : {self.white_score}\n{winning_call}"
                )
            return False

        # 카드 선택 후 드로우
        now_black = self.player1.choose_card(self.board, self.player_black_hand)
        self.player_black_hand.remove(now_black)
        if self.black_cards:
            self.player_black_hand.append(self.black_cards.pop())

        now_white = self.player2.choose_card(self.board, self.player_white_hand)
        self.player_white_hand.remove(now_white)
        if self.white_cards:
            self.player_white_hand.append(self.white_cards.pop())

        # 카드 착수
        order = self.who_place_first(now_black, now_white)

        if self.verbose:
            print(f"Now turn : {self.turn}")
            print('check!!!!!!!!!!!!!!')
            self.print_board()
            print("\n\n")

        if order == 1:
            black_location = self.player1.choose_location_first(self.board, now_black, now_white)
            self.board[black_location] = now_black

            if now_black[0] == 6:
                self.try_special_move(black_location, 1, self.player1)

            white_location = self.player2.choose_location_second(self.board, now_white)
            self.board[white_location] = now_white

            if now_white[0] == 6:
                self.try_special_move(white_location, 2, self.player2)
        else:
            white_location = self.player2.choose_location_first(self.board, now_white, now_black)
            self.board[white_location] = now_white

            if now_white[0] == 6:
                self.try_special_move(white_location, 2, self.player2)

            black_location = self.player1.choose_location_second(self.board, now_black)
            self.board[black_location] = now_black

            if now_black[0] == 6:
                self.try_special_move(black_location, 1, self.player1)

        self.turn += 1
        if self.verbose:
            print(f"Now turn : {self.turn}")
            self.print_board()
            print("Current Score")
            print("Red", self.check_score(1))
            print("Blue", self.check_score(2))
            print("\n\n")

        return True

    def play(self):
        while self.process_turn():
            pass

        if self.check_score(1) > self.check_score(2):
            return 1
        elif self.check_score(1) < self.check_score(2):
            return 2
        else:
            return 3 - self.tiebreaker

    def get_adjacent_same_color_tiles(self, position, color):
        """입력 위치에서 인접한 같은 색의 타일 위치 목록을 반환"""
        return [
            adj
            for adj in self.adjacent[position]
            if self.board[adj][1] == color
        ]

    def get_adjacent_empty_positions(self, position):
        """입력 위치에서 인접한 빈칸 위치 목록을 반환"""
        return [
            adj
            for adj in self.adjacent[position]
            if self.board[adj][1] == 0
        ]