position_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

players = {'X': '', 'O': ''}

player = 'X'
turn_num = 0
game_on = True


def print_board():
    print(position_list[0], position_list[1], position_list[2]+'\n' +
          position_list[3], position_list[4], position_list[5]+'\n' +
          position_list[6], position_list[7], position_list[8]+'\n')


def ask_turn(turn_num):
    if turn_num < 1:
        value = input("Do you want to be X or O?: ")
        if value == 'X':
            players['X'] = 'player 1'
            players['O'] = 'player 2'
        else:
            players['O'] = 'player 1'
            players['X'] = 'player 2'
    else:
        pass
    return turn_num


def check_turn(turn_num):
    if turn_num % 2 == 0:
        print(players['X'])
        turn_num += 1
    else:
        print(players['O'])
        turn_num += 1
    return turn_num


def ask_position():
    position = 'wrong'
    while not position.isdigit() or position not in position_list:
        position = input("Choose position: ")
        if not position.isdigit() or position not in position_list:
            print("Invalid input")

    return position


def replace_position(position):
    if position in position_list:
        position_list[position_list.index(position)] = player


def check_game():

    if position_list[0] == position_list[1] == position_list[2] == player:
        return True
    elif position_list[3] == position_list[4] == position_list[5] == player:
        return True
    elif position_list[6] == position_list[7] == position_list[8] == player:
        return True
    elif position_list[0] == position_list[3] == position_list[6] == player:
        return True
    elif position_list[1] == position_list[4] == position_list[7] == player:
        return True
    elif position_list[2] == position_list[5] == position_list[8] == player:
        return True
    elif position_list[0] == position_list[4] == position_list[8] == player:
        return True
    elif position_list[2] == position_list[4] == position_list[6] == player:
        return True
    elif turn_num == 9:
        return True
    else:
        pass


print_board()
while game_on:
    turn_num = check_turn(ask_turn(turn_num))
    replace_position(ask_position())
    print_board()

    if check_game() and turn_num == 9:
        print('Draw!')
        break
    elif check_game():
        print(players[player] + ' win!!')
        break
    if player == 'X':
        player = 'O'
    else:
        player = 'X'



