import copy

from board_checking import is_terminal_node, get_list_legal_moves
from board_operation import eval_board, execute_move, min_eval_board, max_eval_board


def minimax(current_board, current_player, current_depth, maximizing_player):
    if current_depth == 0 or is_terminal_node(current_board, current_player):
        return eval_board(current_board, current_player)

    legal_moves = get_list_legal_moves(current_board, current_player)

    if maximizing_player:
        best_value = min_eval_board
        for x, y in legal_moves:
            board_temp, _ = execute_move(copy.deepcopy(current_board), x, y, current_player)
            v = minimax(board_temp, current_player, current_depth - 1, False)
            best_value = max(best_value, v)

    else:  # minimizingPlayer
        best_value = max_eval_board
        for x, y in legal_moves:
            board_temp, _ = execute_move(copy.deepcopy(current_board), x, y, current_player)
            v = minimax(board_temp, current_player, current_depth - 1, True)
            best_value = min(best_value, v)

    return best_value
