import random

from board_check import get_list_legal_moves


def random_bot(current_board, current_player):
    legal_moves = get_list_legal_moves(current_board, current_player)
    rand_idx = random.randint(0, len(legal_moves))
    return legal_moves[rand_idx]
