import random

def choose_card(hand):
    choice = random.choice(hand)
    hand.remove(choice)

    return choice

def choose_place(board):
    #착수 가능 지역 탐색
    available_place = []
    for i in range(1,20):
        if board[i][1] == 0:
            available_place.append(i)
    
    #착수할 칸 선택
    random_place_choice = random.choice(available_place)
    return random_place_choice

def draw_card(hand,deck):
    #덱이 비어있으면 안뽑음
    if not deck:
        return
    hand.append(deck.pop())
    return

def start_hand(hand_size,deck):
    hand = []
    for i in range(hand_size):
        hand.append(deck.pop())
    
    return hand

    