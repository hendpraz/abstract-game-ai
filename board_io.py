from board_identity import board_size, board


def print_board():
    m = len(str(board_size - 1))
    for y in range(board_size):
        row = ''
        for x in range(board_size):
            row += board[y][x]
            row += ' ' * m
        print(str(y) + '   ' + row)
    print('Y')
    row = ''
    for x in range(board_size):
        row += str(x).zfill(m) + ' '
    print('  X ' + row + '\n')