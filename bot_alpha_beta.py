import copy

from board_checking import is_legal_move, is_terminal_node
from board_identity import board_size
from board_operation import eval_board, execute_move, min_eval_board, max_eval_board


def alpha_beta(current_board, current_player, current_depth, alpha, beta, maximizing_player):
    if current_depth == 0 or is_terminal_node(current_board, current_player):
        return eval_board(current_board, current_player)

    if maximizing_player:
        v = min_eval_board
        for y in range(board_size):
            for x in range(board_size):
                legal, message = is_legal_move(current_board, x, y, current_player)
                if legal:
                    board_temp, total_piece_taken = execute_move(copy.deepcopy(current_board), x, y, current_player)
                    v = max(v, alpha_beta(board_temp, current_player, current_depth - 1, alpha, beta, False))
                    alpha = max(alpha, v)
                    if beta <= alpha:
                        break  # beta cut-off
        return v

    else:  # minimizingPlayer
        v = max_eval_board
        for y in range(board_size):
            for x in range(board_size):
                legal, message = is_legal_move(current_board, x, y, current_player)
                if legal:
                    board_temp, total_piece_taken = execute_move(copy.deepcopy(current_board), x, y, current_player)
                    v = min(v, alpha_beta(board_temp, current_player, current_depth - 1, alpha, beta, True))
                    beta = min(beta, v)
                    if beta <= alpha:
                        break  # alpha cut-off

        return v
