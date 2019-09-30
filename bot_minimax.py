import copy

from board import is_terminal_node, eval_board, n, is_legal_move, check_move

min_eval_board = -1  # min - 1
max_eval_board = n * n + 4 * n + 4 + 1  # max + 1


def minimax(current_board, current_player, current_depth, maximizing_player):

    if current_depth == 0 or is_terminal_node(current_board, current_player):
        return eval_board(current_board, current_player)

    if maximizing_player:
        best_value = min_eval_board
        for y in range(n):
            for x in range(n):
                if is_legal_move(current_board, x, y, current_player):
                    board_temp, tot_ctr = check_move(copy.deepcopy(current_board), x, y, current_player)
                    v = minimax(board_temp, current_player, current_depth - 1, False)
                    best_value = max(best_value, v)

    else:  # minimizingPlayer
        best_value = max_eval_board
        for y in range(n):
            for x in range(n):
                if is_legal_move(current_board, x, y, current_player):
                    board_temp, tot_ctr = check_move(copy.deepcopy(current_board), x, y, current_player)
                    v = minimax(board_temp, current_player, current_depth - 1, True)
                    best_value = min(best_value, v)

    return best_value
