import copy

n = 8  # board size (even)

board = [['0' for x in range(n)] for y in range(n)]

dir_x = [-1, 0, 1, -1, 1, -1, 0, 1]
dir_y = [-1, -1, -1, 0, 0, 1, 1, 1]


def init_board():
    if n % 2 == 0:  # if board size is even
        z = int((n - 2) / 2)
        board[z][z] = '2'
        board[n - 1 - z][z] = '1'
        board[z][n - 1 - z] = '1'
        board[n - 1 - z][n - 1 - z] = '2'


def print_board():
    m = len(str(n - 1))
    for y in range(n):
        row = ''
        for x in range(n):
            row += board[y][x]
            row += ' ' * m
        print(row + ' ' + str(y))
    print()
    row = ''
    for x in range(n):
        row += str(x).zfill(m) + ' '
    print(row + '\n')


def check_move(current_board, x, y, player):  # assuming valid move
    num_opponent_piece_taken = 0
    current_board[y][x] = player
    for d in range(8):  # 8 directions
        ctr = 0
        for i in range(n):
            dx = x + dir_x[d] * (i + 1)
            dy = y + dir_y[d] * (i + 1)
            if dx < 0 or dx > n - 1 or dy < 0 or dy > n - 1:
                ctr = 0
                break
            elif current_board[dy][dx] == player:
                break
            elif current_board[dy][dx] == '0':
                ctr = 0
                break
            else:
                ctr += 1
        for i in range(ctr):
            dx = x + dir_x[d] * (i + 1)
            dy = y + dir_y[d] * (i + 1)
            current_board[dy][dx] = player
        num_opponent_piece_taken += ctr
    return current_board, num_opponent_piece_taken


def is_legal_move(current_board, x, y, player):
    if x < 0 or x > n - 1 or y < 0 or y > n - 1:
        return False
    if current_board[y][x] != '0':
        return False
    (boardTemp, tot_ctr) = check_move(copy.deepcopy(current_board), x, y, player)
    if tot_ctr == 0:
        return False
    return True


def eval_board(current_board, current_player):
    tot = 0
    for y in range(n):
        for x in range(n):
            if current_board[y][x] == current_player:
                if (x == 0 or x == n - 1) and (y == 0 or y == n - 1):
                    tot += 4  # corner
                elif (x == 0 or x == n - 1) or (y == 0 or y == n - 1):
                    tot += 2  # side
                else:
                    tot += 1
    return tot


def is_terminal_node(current_board, current_player):
    for y in range(n):
        for x in range(n):
            if is_legal_move(current_board, x, y, current_player):
                return False
    return True


def get_sorted_node(current_board, player):
    sorted_nodes = []
    for y in range(n):
        for x in range(n):
            if is_legal_move(current_board, x, y, player):
                (boardTemp, tot_ctr) = check_move(copy.deepcopy(current_board), x, y, player)
                sorted_nodes.append((boardTemp, eval_board(boardTemp, player)))
    sorted_nodes = sorted(sorted_nodes, key=lambda node: node[1], reverse=True)
    sorted_nodes = [node[0] for node in sorted_nodes]
    return sorted_nodes
