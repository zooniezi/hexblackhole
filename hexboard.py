from random import shuffle
import decision, ai_player

#보드판 위의 숫자가 무엇인지 (기본:-1), 무슨 색인지 (빈칸:0 흑:1 백:2)
board = [[-1,0] for i in range(20)]

#각 칸이 인접한 칸이 어디인지
adjacent = [
    [],
    [2,4,5],
    [1,3,5,6],
    [2,6,7],
    [1,5,8,9],
    [1,2,4,6,9,10],
    [2,3,5,7,10,11],
    [3,6,11,12],
    [4,9,13],
    [4,5,8,10,13,14],
    [5,6,9,11,14,15],
    [6,7,10,12,15,16],
    [7,11,16],
    [8,9,14,17],
    [9,10,13,15,17,18],
    [10,11,14,16,18,19],
    [11,12,15,19],
    [13,14,18],
    [14,15,17,19],
    [15,16,18],
]

#같은 숫자를 낸 경우 우선권 선언(기본:1-흑색 우선)
tiebreaker = 1

#점수 계산에 쓰일 변수 선언
black_score = 0
white_score = 0

# 각 플레이어 전체 카드풀 만들기 및 1카드는 서로 반대 색으로 설정하기
black_cards = [[i,1] for i in range(1,12)]
white_cards = [[i,2] for i in range(1,12)]
black_cards[0][1] = 2
white_cards[0][1] = 1

# 카드 덱 섞기
shuffle(black_cards)
shuffle(white_cards)

# 초기 세팅 확인용
decision.print_board(board)
print(black_cards)
print(white_cards)

#게임 시작 전 초기 손패 뽑기
player_black_hand = ai_player.start_hand(3,black_cards)
player_white_hand = ai_player.start_hand(3,white_cards)


#임시 테스트용 변수
temp = 1
game_notation = [tiebreaker]
#게임 진행
while True:
    #한칸만 비어있는 경우 점수 계산 및 게임 종료
    if decision.game_over(board):
        decision.blackhole_swallow(board,adjacent)
        black_score = decision.check_score(board,adjacent,1)
        white_score = decision.check_score(board,adjacent,2)
        winning_call = ""

        if black_score>white_score:
            winning_call = "Black wins"
        elif black_score<white_score:
            winning_call = "White wins"
        else:
            winning_call = "Draw"

        print("Result")
        decision.print_board(board)
        print()
        print()
        print(f'Total Score\nBlack : {black_score}\nWhite : {white_score}\n{winning_call}')
        break
    
    #임시용 코드 (무작위로 뽑아 무작위로 배치)
    now_black = ai_player.choose_card(player_black_hand)
    ai_player.draw_card(now_black,player_black_hand,black_cards)

    now_white = ai_player.choose_card(player_white_hand)
    ai_player.draw_card(now_white,player_white_hand,white_cards)

    board[ai_player.choose_place(board)] = decision.who_place_first(now_black,now_white,tiebreaker)[0]
    board[ai_player.choose_place(board)] = decision.who_place_first(now_black,now_white,tiebreaker)[1]
    
    temp+=2
    print(f'Now turn : {temp//2+1}\n\n')
    decision.print_board(board)
    print()
    print('Current Score')
    print('Black' , decision.check_score(board,adjacent,1))
    print('White',decision.check_score(board,adjacent,2))
    print()
    print()
    print()

