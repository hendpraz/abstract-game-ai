import copy

board_size = 8

board = [['0' for x in range(board_size)] for y in range(board_size)]

dir_x = [-1, 0, 1, -1, 1, -1, 0, 1]
dir_y = [-1, -1, -1, 0, 0, 1, 1, 1]


def init_board():
    if board_size % 2 == 0:
        z = int((board_size - 2) / 2)
        board[z][z] = '2'
        board[board_size - 1 - z][z] = '1'
        board[z][board_size - 1 - z] = '1'
        board[board_size - 1 - z][board_size - 1 - z] = '2'


def print_board():
    m = len(str(board_size - 1))
    for y in range(board_size):
        row = ''
        for x in range(board_size):
            row += board[y][x]
            row += ' ' * m
        print(row + ' ' + str(y))
    print()
    row = ''
    for x in range(board_size):
        row += str(x).zfill(m) + ' '
    print(row + '\n')


def execute_move(current_board, x, y, player):  # assuming valid move
    num_opponent_piece_taken = 0
    current_board[y][x] = player
    for d in range(8):  # 8 directions
        ctr = 0
        for i in range(board_size):
            dx = x + dir_x[d] * (i + 1)
            dy = y + dir_y[d] * (i + 1)
            if dx < 0 or dx > board_size - 1 or dy < 0 or dy > board_size - 1:
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
    if x < 0 or x > board_size - 1 or y < 0 or y > board_size - 1:
        return False
    if current_board[y][x] != '0':
        return False
    (boardTemp, tot_ctr) = execute_move(copy.deepcopy(current_board), x, y, player)
    if tot_ctr == 0:
        return False
    return True


def eval_board(current_board, current_player):
    tot = 0
    for y in range(board_size):
        for x in range(board_size):
            if current_board[y][x] == current_player:
                if (x == 0 or x == board_size - 1) and (y == 0 or y == board_size - 1):
                    tot += 4  # corner
                elif (x == 0 or x == board_size - 1) or (y == 0 or y == board_size - 1):
                    tot += 2  # side
                else:
                    tot += 1
    return tot


def is_terminal_node(current_board, current_player):
    for y in range(board_size):
        for x in range(board_size):
            if is_legal_move(current_board, x, y, current_player):
                return False
    return True


class Board:

    def __init__(self):
        self.__board_size = 8
        self.__board = [['0' for x in range(board_size)] for y in range(board_size)]
        self.__dir_x = [-1, 0, 1, -1, 1, -1, 0, 1]
        self.__dir_y = [-1, -1, -1, 0, 0, 1, 1, 1]


