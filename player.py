import random


class Player:
    def __init__(self):
        pass

    def choose_card(self, board, hand):
        pass

    def choose_location_first(self, board, my_card, op_card):
        pass

    def choose_location_second(self, board, my_card):
        pass


class RandomPlayer(Player):
    def __init__(self) -> None:
        pass

    def choose_card(self, board, hand):
        choice = random.choice(hand)
        return choice

    def choose_location_first(self, board, my_card, op_card):
        # 착수 가능 지역 탐색
        available_place = []
        for i in range(1, 20):
            if board[i][1] == 0:
                available_place.append(i)

        # 착수할 칸 선택
        random_place_choice = random.choice(available_place)
        return random_place_choice

    def choose_location_second(self, board, my_card):
        # 착수 가능 지역 탐색
        available_place = []
        for i in range(1, 20):
            if board[i][1] == 0:
                available_place.append(i)

        # 착수할 칸 선택
        random_place_choice = random.choice(available_place)
        return random_place_choice
