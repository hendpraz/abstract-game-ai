from board_identity import board_size


def is_corner_cell(x, y):
    return (x == 0 or x == board_size - 1) and (y == 0 or y == board_size - 1)


def is_side_cell(x, y):
    return (x == 0 or x == board_size - 1) or (y == 0 or y == board_size - 1)
