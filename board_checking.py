import copy

from board_identity import board_size
from board_operation import execute_move


def is_legal_move(current_board, x, y, player):
    if not (0 <= x < board_size and 0 <= y < board_size):
        return False, 'Out of range'

    if current_board[y][x] != '0':
        return False, 'Box is filled'

    board_temp, total_piece_taken = execute_move(copy.deepcopy(current_board), x, y, player)
    if total_piece_taken == 0:
        return False, 'No piece taken!'

    return True, 'OK'


def is_terminal_node(current_board, current_player):
    for y in range(board_size):
        for x in range(board_size):
            legal, message = is_legal_move(current_board, x, y, current_player)
            if legal:
                return False

            legal, message = is_legal_move(current_board, x, y, current_player)
            if legal:
                return False
    return True
