from board_checking import is_legal_move
from board_helper import is_corner_cell, is_side_cell
from board_identity import board_size, board, dir_x, dir_y


def init_fill_center_board():
    # c == center
    c_low = int((board_size - 2) / 2)
    c_high = board_size - 1 - c_low

    board[c_low][c_low] = '2'
    board[c_high][c_low] = '1'
    board[c_low][c_high] = '1'
    board[c_high][c_high] = '2'


def execute_move(current_board, x, y, player):
    # I.S : player going to <x,y> is a valid move

    num_opponent_piece_taken = 0
    current_board[y][x] = player

    for d in range(8):  # 8 directions
        piece_taken = 0

        for i in range(board_size):
            dx = x + dir_x[d] * (i + 1)
            dy = y + dir_y[d] * (i + 1)

            if not (0 <= dx < board_size and 0 <= dy < board_size):
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
            dx = x + dir_x[d] * (i + 1)
            dy = y + dir_y[d] * (i + 1)
            current_board[dy][dx] = player

        num_opponent_piece_taken += piece_taken

    return current_board, num_opponent_piece_taken


def eval_board(current_board, current_player):
    score = 0
    for y in range(board_size):
        for x in range(board_size):
            if current_board[y][x] == current_player:
                if is_corner_cell(x, y):
                    score += 4
                elif is_side_cell(x, y):
                    score += 2
                else:
                    score += 1
    return score


min_eval_board = -1  # min - 1
max_eval_board = board_size * board_size + 4 * board_size + 4 + 1  # max + 1


def get_list_legal_moves(current_board, current_player):
    legal_moves = []
    for y in range(board_size):
        for x in range(board_size):
            legal, message = is_legal_move(current_board, x, y, current_player)
            if legal:
                legal_moves.append((x, y))
    return legal_moves
