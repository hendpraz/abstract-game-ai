import copy


from board import execute_move, is_legal_move, n
from bot_alpha_beta import alpha_beta
from bot_minimax import minimax

min_eval_board = -1  # min - 1
max_eval_board = n * n + 4 * n + 4 + 1  # max + 1


def best_move(current_board, current_player, cpu_mode, deepest_depth):

    points, max_points = 0, 0
    x_move_to, y_move_to = -1, -1

    for y in range(n):
        for x in range(n):

            if is_legal_move(current_board, x, y, current_player):
                board_temp, total_piece_taken = execute_move(copy.deepcopy(current_board), x, y, current_player)

                if cpu_mode == 1:
                    points = minimax(board_temp, current_player, deepest_depth, True)
                elif cpu_mode == 2:
                    points = alpha_beta(current_board, current_player, deepest_depth,
                                        min_eval_board, max_eval_board, True)

                if points > max_points:
                    max_points = points
                    x_move_to, y_move_to = x, y

    return x_move_to, y_move_to
