import copy

from board_processing import execute_move
from board_identity import board_size


def is_cell_outside(x, y):
    return not(0 < x < board_size and 0 < y < board_size)


def is_legal_move(current_board, x, y, player):
    if is_cell_outside(x, y):
        return False

    if current_board[y][x] != '0':
        return False

    board_temp, total_piece_taken = execute_move(copy.deepcopy(current_board), x, y, player)
    if total_piece_taken == 0:
        return False

    return True


def get_list_legal_moves(current_board, current_player):
    r = range(board_size)
    return [(x, y) for x in r for y in r if is_legal_move(current_board, x, y, current_player)]


def is_terminal_node(current_board, current_player):
    legal_moves = get_list_legal_moves(current_board, current_player)
    return len(legal_moves) > 0