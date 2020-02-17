game_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def place_num():
    find = find_empty()
    if not find:
        return True
    else:
        row, col = find

    for x in range(1, 10):
        if is_valid(x, (row, col)):
            game_board[row][col] = x

            if place_num():
                return True

            game_board[row][col] = 0

    return False


def is_valid(num, pos):
    rlist = game_board[pos[0]]
    clist = []
    for x in range(len(game_board)):
        clist.append(game_board[x][pos[1]])

    if num not in rlist:
        if num not in clist:
            return True

        else:
            return False
    else:
        return False


def print_board():
    print("\n")
    for x in range(len(game_board)):
        count = 0
        if (x % 3) == 0 and x != 0:
            print("-  " * 11)
        for i in range(len(game_board[x])):
            if i % 3 == 0 and i != 0:
                print(end="|  ")

            if i == 8:
                print(str(game_board[x][count]))
            else:
                print(end=str(game_board[x][count]) + "  ")

            count += 1


def find_empty():
    for x in range(len(game_board)):
        count = 0
        for i in range(len(game_board[x])):
            if game_board[x][count] == 0:
                return x, count
            count += 1


print_board()
place_num()
print_board()


