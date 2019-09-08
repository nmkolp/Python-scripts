board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
x = 0
y = 0
player = 1


def check_win():
    if board[x][0] == board[x][1] == board[x][2] != 0:
        return True
    if board[0][y] == board[1][y] == board[2][y] != 0:
        return True
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return True
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return True
    return False


def check_no_moves_left():
    for x in range(3):
        for y in range(3):
            if board[x][y] == 0:
                return False
    return True


def print_board():
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


def set_coords(i):
    if i < 1 or i > 9:
        return False
    global x
    x = (i - 1) % 3
    global y
    y = 2 - (i - 1) // 3
    return True


print_board()
while True:
    while True:
        inp = input("Enter: ")
        if inp.isdigit() and set_coords(int(inp)) and board[x][y] == 0:
            break
    board[x][y] = player
    print_board()
    if check_win():
        print("Congratulations")
        break
    if check_no_moves_left():
        print("Draw")
        break
    player = -player
