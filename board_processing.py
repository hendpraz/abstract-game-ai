from board_identity import board_size, board, adj_x, adj_y


def init_board():
    # c == center
    c_low = int((board_size - 2) / 2)
    c_high = board_size - 1 - c_low

    board[c_low][c_low] = '2'
    board[c_high][c_low] = '1'
    board[c_low][c_high] = '1'
    board[c_high][c_high] = '2'


def execute_move(current_board, x, y, player):
    # I.S : Move to <X,Y> is a valid move.

    num_opponent_piece_taken = 0
    current_board[y][x] = player

    for d in range(8):  # 8 directions
        piece_taken = 0

        for i in range(board_size):
            dx = x + adj_x[d] * (i + 1)
            dy = y + adj_y[d] * (i + 1)

            if not(0 < dx < board_size and 0 < dy < board_size):
                piece_taken = 0
                break
            elif current_board[dy][dx] == player:
                break
            elif current_board[dy][dx] == '0':
                piece_taken = 0
                break
            else:
                piece_taken += 1

        for i in range(piece_taken):
            dx = x + adj_x[d] * (i + 1)
            dy = y + adj_y[d] * (i + 1)
            current_board[dy][dx] = player

        num_opponent_piece_taken += piece_taken

    return current_board, num_opponent_piece_taken


