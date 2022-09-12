import random #Импорт модуля random для игры против компьютера
board = list(' ' * 9) #Состояние доски
mark = 'X' #Маркер игрока
winning_combinations = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
comp = None #Желает ли пользователь сыграть против компьютера
iteration = 0 #Номер итерации

def greeting():#Приветствие игрока
    global comp
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    comp = input('Хотите сыграть против компьютера? Y/N ') in ('Y', 'y', 'Н', 'н')
    print("-------------------")
    print("формат ввода: цифра")
    print("  от 1 до 9 как на ")
    print("     клавиатуре    ")
    print("мобильного телефона")
    print("-------------------")
    
def print_board():#Рисует игральную доску
    print("-----------")
    for i, j in enumerate(board):
        if (i+1) % 3 != 0:
            print(f' {j} ', end='|')
        else:
            print(f' {j} ', end='\n')
            print("-----------")
            
def computer_choice(): #Компьютер ставит маркер
    empty_places = list(i for i, j in enumerate(board) if j == ' ')
    computer_choice = random.choice(empty_places)
    print('Компьютер делает ход')
    board[computer_choice] = mark

def player_choice(): #Игрок выбирает ячейку и вызывается исключение при необходимости
    print(f'Введите номер поля, куда вы хотите поставить знак {mark} ', end='')
    while True:
        try:
            player_choice = int(input())
            if player_choice not in range(1,10):
                print('Нужно ввести цифру от 1 до 9. Попробуйте ещё раз')
                continue
            elif board[player_choice-1] != ' ':
                print('Выбранная ячейка занята. Попробуйте ещё раз')
                continue
            else:
                board[player_choice-1] = mark
                break
        except Exception:
            print('Нужно ввести цифру от 1 до 9. Попробуйте ещё раз')

def check_win():#Сверяются выигрышные комбинации с комбинацией игрока
    combination = list(i for i, j in enumerate(board) if j == mark)
    for a in winning_combinations:
        x = 0
        for b in a: 
            if b in combination:
                x += 1
                if x == 3:
                    print(f'Игрок {mark} победил')
                    return True

def check_draw(): #Проверка на ничью
    global iteration
    if iteration == 8:
        print('Ничья')
        return True
    else:
        iteration += 1

def change_mark():#Изменение маркера
    global mark
    if mark == 'X':
        mark = 'O'
    else:
        mark = 'X'
        
greeting()
print_board()
while True:
    if comp and mark == 'O':
        computer_choice()
    else:
        player_choice()
    print_board()
    if check_win() or check_draw():
        break
    change_mark()

