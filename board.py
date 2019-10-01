import copy
import tkinter

board_size = 8

global buttons

board = [['0' for x in range(board_size)] for y in range(board_size)]

dir_x = [-1, 0, 1, -1, 1, -1, 0, 1]
dir_y = [-1, -1, -1, 0, 0, 1, 1, 1]


def init_board():
    # c == center
    c_low = int((board_size - 2) / 2)
    c_high = board_size - 1 - c_low

    board[c_low][c_low] = '2'
    board[c_high][c_low] = '1'
    board[c_low][c_high] = '1'
    board[c_high][c_high] = '2'


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
        piece_taken = 0

        for i in range(board_size):
            dx = x + dir_x[d] * (i + 1)
            dy = y + dir_y[d] * (i + 1)

            if not(0 < dx < board_size and 0 < dy < board_size):
                piece_taken = 0
                break
            elif current_board[dy][dx] == player:
                break
            elif current_board[dy][dx] == '0':
                piece_taken = 0
                break
            else:
                piece_taken += 1

        for i in range(piece_taken):
            dx = x + dir_x[d] * (i + 1)
            dy = y + dir_y[d] * (i + 1)
            current_board[dy][dx] = player

        num_opponent_piece_taken += piece_taken

    return current_board, num_opponent_piece_taken


def is_legal_move(current_board, x, y, player):
    if not(0 < x < board_size and 0 < y < board_size):
        return False

    if current_board[y][x] != '0':
        return False

    board_temp, total_piece_taken = execute_move(copy.deepcopy(current_board), x, y, player)
    if total_piece_taken == 0:
        return False

    return True


def eval_board(current_board, current_player):
    score = 0
    for y in range(board_size):
        for x in range(board_size):
            if current_board[y][x] == current_player:
                if (x == 0 or x == board_size - 1) and (y == 0 or y == board_size - 1):
                    score += 4  # corner
                elif (x == 0 or x == board_size - 1) or (y == 0 or y == board_size - 1):
                    score += 2  # side
                else:
                    score += 1
    return score


def is_terminal_node(current_board, current_player):
    for y in range(board_size):
        for x in range(board_size):
            if is_legal_move(current_board, x, y, current_player):
                return False
    return True