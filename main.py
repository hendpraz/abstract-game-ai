import os

from engine import best_move
from board import init_board, print_board, check_move, is_legal_move, board, eval_board, is_terminal_node


if __name__ == '__main__':

    print('OTHELLO BOARD GAME')
    print('1: Minimax')
    print('2: Minimax w/ Alpha-Beta Pruning')
    print('3: Random Bot')
    cpu_mode = int(input('Select AI Algorithm: '))

    deepest_depth = 0
    if 0 < cpu_mode < 4:
        deepest_depth = 4
        depthStr = input('Select Search Depth (DEFAULT: 4): ')
        if depthStr != '':
            deepest_depth = int(deepest_depth)

    print('\n1: User 2: AI (Just press Enter for Exit!)')

    init_board()
    while True:

        for p in range(2):

            print()
            print_board()

            player = str(p + 1)
            print('PLAYER: ' + player)

            if is_terminal_node(board, player):
                print('Player cannot play! Game ended!')
                print('Score User: ' + str(eval_board(board, '1')))
                print('Score AI  : ' + str(eval_board(board, '2')))
                os.exit(0)

            if player == '1':  # user's turn
                while True:
                    x, y = map(int, input('X Y: ').split())

                    if is_legal_move(board, x, y, player):
                        board, total_piece_taken = check_move(board, x, y, player)
                        print('# of pieces taken: ' + str(total_piece_taken))
                        break
                    else:
                        print('Invalid move! Try again!')

            else:  # AI's turn
                x, y = best_move(board, player, cpu_mode, deepest_depth)
                if not x == -1 and y == -1:
                    board, total_piece_taken = check_move(board, x, y, player)
                    print('AI played (X Y): ' + str(x) + ' ' + str(y))
                    print('# of pieces taken: ' + str(total_piece_taken))
