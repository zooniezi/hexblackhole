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


class HumanPlayer:
    def __init__(self):
        pass
    
    def check_continue(self):
        print("type any key to continue",end="")
        input()
        return

    def choose_card(self, board, hand):
        print("Choose card you want to place this turn.")

        # 글씨 색상 설정을 위한 함수
        def colored_text(value, color_code):
            return f"\033[{color_code}m{value}\033[0m"

        def get_colored_value(i):
            if hand[i][1] == 1:
                return colored_text(hand[i][0], 91)  # 빨간색(흑)
            elif hand[i][1] == 2:
                return colored_text(hand[i][0], 94)  # 파란색(백)
            else:
                return colored_text(hand[i][0], 93)  # 노란색(빈칸)

        print(
            "Your cards : ",
            get_colored_value(0),
            get_colored_value(1),
            get_colored_value(2),
            "\n",
        )
        a = "4"
        temp = [hand[i][0] for i in range(3)]
        while True:
            print("Which card do you want to pick? : ", end="")
            a = input()
            b = int(a)
            if b == hand[0][0]:
                return hand[0]
            elif b == hand[1][0]:
                return hand[1]
            elif b == hand[2][0]:
                return hand[2]
            else:
                print("It's unavailable value, please type again.")
        return

    def choose_location_first(self, board, my_card, op_card):
        # 착수 가능 지역 탐색
        available_place = []
        for i in range(1, 20):
            if board[i][1] == 0:
                available_place.append(i)

        print("It's your turn. Where would you place your card?")

        print("Fill in the number of any of the blanks that are colored yellow.")
        print("\nType the number : ", end="")
        idx = int(input())

        while True:
            if idx in available_place:
                print(f"You choose place number {idx}.\n\n")
                break
            else:
                print("It's unavailable value, please type again.")
                print("\nType the number : ", end="")
                idx = int(input())

        return idx

    def choose_location_second(self, board, my_card):
        # 착수 가능 지역 탐색
        available_place = []
        for i in range(1, 20):
            if board[i][1] == 0:
                available_place.append(i)

        print("It's your turn. Where would you place your card?")

        print("Fill in the number of any of the blanks that are colored yellow.")
        print("\nType the number : ", end="")
        idx = int(input())

        while True:
            if idx in available_place:
                print(f"You choose place number {idx}.\n\n")
                break
            else:
                print("It's unavailable value, please type again.")
                print("\nType the number : ", end="")
                idx = int(input())

        return idx


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
