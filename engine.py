import copy

from board_checking import is_legal_move
from board_identity import board_size
from board_operation import execute_move, min_eval_board, max_eval_board
from bot_alpha_beta import alpha_beta
from bot_minimax import minimax
from bot_random import random_bot


def best_move(current_board, current_player, cpu_mode, deepest_depth):
    points, max_points = 0, 0
    x_move_to, y_move_to = -1, -1

    for y in range(board_size):
        for x in range(board_size):
            legal, message = is_legal_move(current_board, x, y, current_player)
            if legal:
                board_temp, total_piece_taken = execute_move(copy.deepcopy(current_board), x, y, current_player)

                if cpu_mode == 1:
                    points = minimax(board_temp, current_player, deepest_depth, True)
                elif cpu_mode == 2:
                    points = alpha_beta(current_board, current_player, deepest_depth,
                                        min_eval_board, max_eval_board, True)
                elif cpu_mode == 3:
                    return random_bot(current_board, current_player)

                if points > max_points:
                    max_points = points
                    x_move_to, y_move_to = x, y

    return x_move_to, y_move_to
