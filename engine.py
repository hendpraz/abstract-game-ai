import copy


from board import check_move, is_legal_move, n, eval_board
from bot_alpha_beta import alpha_beta
from bot_minimax import minimax

min_eval_board = -1  # min - 1
max_eval_board = n * n + 4 * n + 4 + 1  # max + 1


def best_move(current_board, current_player, opt, deepest_depth):
    points = 0
    max_points = 0
    mx = -1
    my = -1
    for y in range(n):
        for x in range(n):
            if is_legal_move(current_board, x, y, current_player):
                board_temp, tot_ctr = check_move(copy.deepcopy(current_board), x, y, current_player)
                if opt == 0:
                    points = eval_board(board_temp, current_player)
                elif opt == 1:
                    points = minimax(board_temp, current_player, deepest_depth, True)
                elif opt == 2:
                    points = alpha_beta(current_board, current_player, deepest_depth, min_eval_board, max_eval_board, True)
                if points > max_points:
                    max_points = points
                    mx = x
                    my = y
    return mx, my


