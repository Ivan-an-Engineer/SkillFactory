board = list([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
mark = 'X'
winning_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
win = False

def print_board():
    global board
    for i, _ in enumerate(board):
        if (i+1) % 3 != 0:
            print(_, end='|')
        else:
            print(_, end='\n') 

def player_choice(mark):
    global board
    player_choice = int(input(f'Введите номер поля, куда вы хотите поставить знак {mark}'))
    if board[player_choice-1] == ' ':
        board[player_choice-1] = mark
    else:
        print('Введенное поле занято, на этот раз пропускаете ход')

def change_mark():
    global mark
    if mark == 'X':
        mark = 'O'
    else:
        mark = 'X'

def evaluation(winning_combinations, mark, board):
    global win
    combination = list([i for i, _ in enumerate(board) if _==mark])
    print(combination)
    for a in winning_combinations:
        x = 0
        for b in a: 
            if b in combination:
                x += 1
                if x == 3:
                    win = True
                    print_board()
                    print('Вы победили')
                    break

while win == False:
    print_board()
    player_choice(mark)
    evaluation(winning_combinations, mark, board)
    change_mark()

