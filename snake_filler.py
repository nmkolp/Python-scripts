l = [[0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0]]


def print_list():
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] < 10:
                print(l[i][j], end="  ")
            else:
                print(l[i][j], end=" ")
        print("")
    print("")


count = 0
for i in range(len(l) // 2 + len(l) % 2):
    for j in range(i, len(l[i]) - i):
        l[i][j] = count
        count += 1
        print_list()
    for j in range(1 + i, len(l) - i):
        if l[j][-1 - i] != 0:
            continue
        l[j][-1 - i] = count
        count += 1
        print_list()
    for j in range(len(l[-1 - i]) - 2 - i, -1 + i, -1):
        l[-1 - i][j] = count
        count += 1
        print_list()
    for j in range(len(l) - 2 - i, i, -1):
        if l[j][i] != 0:
            continue
        l[j][i] = count
        count += 1
        print_list()
