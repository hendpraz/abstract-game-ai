from board_identity import board_size


def is_cell_corner(x, y):
    return (x == 0 or x == board_size - 1) and (y == 0 or y == board_size - 1)


def is_cell_side(x, y):
    return (x == 0 or x == board_size - 1) or (y == 0 or y == board_size - 1)


def eval_board(current_board, current_player):
    score = 0
    for y in range(board_size):
        for x in range(board_size):
            if current_board[y][x] == current_player:
                if is_cell_corner(x, y):
                    score += 4
                elif is_cell_side(x, y):
                    score += 2
                else:
                    score += 1
    return score
