import socket


def create_game():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(server_address)
    sock.listen(1)
    print("Waiting for a player to join the game...")
    global conn
    conn, _ = sock.accept()


def join_game():
    global conn
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(server_address)


def check_placement(board, x, y):
    if x < 0 or y < 0 or x >= len(board[0]) or y >= len(board):
        return False
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if x + dx < 0 or y + dy < 0 or x + dx >= len(board[0]) or y + dy >= len(board):
                continue
            if board[x + dx][y + dy] == 1:
                return False
    return True


def print_board(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[x][y] == 0:
                print("_", end=" ")
            elif board[x][y] == 1:
                print("o", end=" ")
            elif board[x][y] == 2:
                print("x", end=" ")
            elif board[x][y] == -1:
                print("m", end=" ")


while True:
    while True:
        print("Enter command:")
        print("1: create")
        print("2: join")
        print("3: quit")
        command = input(">>> ")
        if command == "1" or command == "create" \
                or command == "2" or command == "join" \
                or command == "3" or command == "quit":
            break
        print("")

    conn = None
    play_first = ""

    if command == "1" or command == "create":
        while True:
            play_first = input("Play first? (y/n): ")
            if play_first == "y" or play_first == "Y" or play_first == "n" or play_first == "N":
                break
        server_address = (input("Enter your IP address: "), 10000)
        create_game()
        conn.send(play_first)
    elif command == "2" or command == "join":
        server_address = (input("Enter server IP address: "), 10000)
        join_game()
        play_first = eval(repr(conn.recv(2)))
        if play_first == "y" or play_first == "Y":
            play_first = "N"
        else:
            play_first = "Y"
    else:
        break

    if conn is None:
        print("Connection failed\n")
        continue

    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    enemy_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    size = 4
    while size > 0:
        for _ in range(size):
            print_board(board)
            print("Place %d-cell ship:" % size)
            while True:
                # TODO change coordinates to LD
                coord = input("Enter coordinates (x:y) or reset: ")
                if coord == "reset":
                    for x in range(len(board[0])):
                        for y in range(len(board)):
                            board[x][y] = 0
                    continue
                x, y = list(map(int, coord.split(":")))
                if not check_placement(board, x, y):
                    print("Wrong input\n")
                    continue
                direction = input("Enter direction (u, d, l, r): ")
                if direction != "U" or direction != "u" \
                        or direction != "D" or direction != "d" \
                        or direction != "L" or direction != "l" \
                        or direction != "R" or direction != "r":
                    print("Wrong input\n")
                    continue
                valid_placement = True
                for i in range(1, size):
                    if direction == "U" or direction == "u":
                        if not check_placement(board, x, y + i):
                            valid_placement = False
                            break
                    elif direction != "D" or direction != "d":
                        if not check_placement(board, x, y - i):
                            valid_placement = False
                            break
                    elif direction != "L" or direction != "l":
                        if not check_placement(board, x - i, y):
                            valid_placement = False
                            break
                    elif direction != "R" or direction != "r":
                        if not check_placement(board, x + i, y):
                            valid_placement = False
                            break
                if not valid_placement:
                    print("Wrong input\n")
                    continue
                for i in range(0, size):
                    if direction == "U" or direction == "u":
                        board[x][y + i] = 1
                    elif direction != "D" or direction != "d":
                        board[x][y - i] = 1
                    elif direction != "L" or direction != "l":
                        board[x - i][y] = 1
                    elif direction != "R" or direction != "r":
                        board[x + i][y] = 1
                break
        size -= 1
