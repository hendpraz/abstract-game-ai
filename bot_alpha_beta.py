import copy

from board_checking import is_legal_move, is_terminal_node
from board_identity import board_size
from board_operation import eval_board, execute_move

min_eval_board = -1  # min - 1
max_eval_board = board_size * board_size + 4 * board_size + 4 + 1  # max + 1


def alpha_beta(current_board, current_player, current_depth, alpha, beta, maximizing_player):
    if current_depth == 0 or is_terminal_node(current_board, current_player):
        return eval_board(current_board, current_player)

    if maximizing_player:
        v = min_eval_board
        for y in range(board_size):
            for x in range(board_size):
                legal, message = is_legal_move(current_board, x, y, current_player)
                if legal:
                    (boardTemp, tot_ctr) = execute_move(copy.deepcopy(current_board), x, y, current_player)
                    v = max(v, alpha_beta(boardTemp, current_player, current_depth - 1, alpha, beta, False))
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
                    (boardTemp, tot_ctr) = execute_move(copy.deepcopy(current_board), x, y, current_player)
                    v = min(v, alpha_beta(boardTemp, current_player, current_depth - 1, alpha, beta, True))
                    beta = min(beta, v)
                    if beta <= alpha:
                        break  # alpha cut-off

        return v
