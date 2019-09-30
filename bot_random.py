import random

from board import board_size, is_legal_move


def get_list_legal_moves(current_board, current_player):
    legal_moves = []
    for y in range(board_size):
        for x in range(board_size):
            if is_legal_move(current_board, x, y, current_player):
                legal_moves.append((x, y))
    return legal_moves


def random_bot(current_board, current_player):
    legal_moves = get_list_legal_moves(current_board, current_player)
    rand_idx = random.randint(0, len(legal_moves))

    print(legal_moves)
    print(rand_idx, legal_moves[rand_idx])

    return legal_moves[rand_idx]
