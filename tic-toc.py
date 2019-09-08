import copy


def check_win(board):
    for y in range(3):
        if board[0][y] == board[1][y] == board[2][y] != 0:
            return True
    for x in range(3):
        if board[x][0] == board[x][1] == board[x][2] != 0:
            return True
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return True
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return True
    return False


def check_no_moves_left(board):
    for x in range(3):
        for y in range(3):
            if board[x][y] == 0:
                return False
    return True


def get_coords(i):
    if i < 1 or i > 9:
        return False
    return [(i - 1) % 3, 2 - (i - 1) // 3]


def print_board(board):
    for y in range(3):
        for x in range(3):
            if board[x][y] == 0:
                print("_", end='')
            elif board[x][y] == 1:
                print("x", end='')
            else:
                print("o", end='')
            if x != 2:
                print(" ", end='')
        print("")
    print("")


def eval_game(board, player):
    if check_no_moves_left(board):
        return [0]
    for x in range(3):
        for y in range(3):
            if board[x][y] == 0:
                nb = copy.deepcopy(board)
                nb[x][y] = player
                if check_win(nb):
                    return [player, x, y]
                eval_result = eval_game(nb, -player)
                if eval_result[0] == player:
                    return [player, x, y]
                if eval_result[0] == 0:
                    ret_val = [0, x, y]
                elif 'ret_val' not in vars():
                    ret_val = [-player, x, y]
    return ret_val


def player_move(board, player):
    while True:
        inp = input("Enter: ")
        if inp.isdigit() and int(inp) != 0:
            coords = get_coords(int(inp))
            x = coords[0]
            y = coords[1]
            if board[x][y] == 0:
                board[x][y] = player
                break


def ai_move(board, player):
    eval_result = eval_game(board, player)
    x = eval_result[1]
    y = eval_result[2]
    board[x][y] = player


play_game = True
while play_game:
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    player = 1
    ai_turn = False

    while True:
        first = input("Play first? (Y/N): ")
        if first == "y" or first == "Y":
            break
        elif first == "n" or first == "N":
            ai_turn = True
            break

    print_board(board)
    while True:
        if ai_turn:
            ai_move(board, player)
        else:
            player_move(board, player)
        print_board(board)
        if check_win(board):
            if ai_turn:
                print("You lost")
            else:
                print("Congratulations")
            break
        if check_no_moves_left(board):
            print("Draw")
            break
        ai_turn = not ai_turn
        player = -player
    print("")

    while True:
        first = input("Play again? (Y/N): ")
        if first == "y" or first == "Y":
            break
        elif first == "n" or first == "N":
            play_game = False
            break
