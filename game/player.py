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
    
    def choose_relocation(self, board, movable_tiles, destination_tiles):
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

    def choose_relocation(self, board, movable_tiles, destination_tiles, six_pos):
        if not movable_tiles or not destination_tiles:
            print("\n※ The ability cannot be used because there are no moveable tiles or empty spaces.")
            return None

        # 색상 및 출력 설정
        color = board[six_pos][1]
        color_code = 91 if color == 1 else 94
        color_name = "Red" if color == 1 else "Blue"

        def colored_text(value, code):
            return f"\033[{code}m{value}\033[0m"

        print(f"\n=== Activate special effect of 6! ===")
        print(f"{colored_text(color_name, color_code)} player can activate the effect of 6.")
        print("You can move one of the same-colored tiles")
        print("adjacent to tile 6 to the blank space around tile 6.")
        print("If you don't want to, enter 0.")

        # 숫자 → 위치 매핑 구성
        number_to_pos = {}
        for pos in movable_tiles:
            tile_number = board[pos][0]
            number_to_pos[tile_number] = pos

        # 표시
        movable_str = ", ".join(colored_text(str(num), color_code) for num in number_to_pos.keys())
        print("Movable tile numbers (same color):", movable_str)

        # 사용자 입력 (숫자 기반)
        user_input = input("Enter the number of tiles you want to move (or cancel if you enter 0): ")
        if user_input == "0":
            print("You canceled activation")
            return None

        try:
            picked_number = int(user_input)
            if picked_number not in number_to_pos:
                raise ValueError
            from_pos = number_to_pos[picked_number]
        except:
            print("Invalid input. Cancel triggering the ability.")
            return None

        # 목적지 선택
        def get_adjacent_empty(pos):
            adjacent = [
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
            return [i for i in adjacent[six_pos] if board[i][1] == 0]

        valid_dests = get_adjacent_empty(six_pos)
        if not valid_dests:
            print("Can't be moved because there are no adjacent spaces near 6.")
            return None

        print("Possible destinations (blank space around tile 6):", valid_dests)
        to_pos = int(input("Enter the location number you want to move to:"))
        if to_pos not in valid_dests:
            print("Invalid location. Cancel ability activation.")
            return None

        return (from_pos, to_pos)


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
    
    def choose_relocation(self, board, movable_tiles, destination_tiles, six_pos):
        if not movable_tiles or not destination_tiles:
            return None

        # 6번 타일 주변의 빈 칸만 목적지로 허용
        adjacent = [
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

        valid_dests = [i for i in adjacent[six_pos] if board[i][1] == 0]
        if not valid_dests:
            return None

        from_pos = random.choice(movable_tiles)
        to_pos = random.choice(valid_dests)
        return (from_pos, to_pos)

