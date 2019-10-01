import sys

from board.checking import is_terminal_node
from board.identity import board
from board.io import print_board
from board.operation import init_fill_center_board, execute_move, eval_board
from bot.engine import best_move

if __name__ == '__main__':

    print('OTHELLO BOARD GAME')
    print('1: Minimax')
    print('2: Minimax w/ Alpha-Beta Pruning')
    print('3: Random Bot')
    cpu_mode1 = int(input('Select 1st AI Algorithm: '))

    print('OTHELLO BOARD GAME')
    print('1: Minimax')
    print('2: Minimax w/ Alpha-Beta Pruning')
    print('3: Random Bot')
    cpu_mode2 = int(input('Select 2nd AI Algorithm: '))

    deepest_depth = 0
    if 0 < cpu_mode1 < 4 and 0 < cpu_mode2 < 4:
        deepest_depth = 4
        depthStr = input('Select Search Depth (DEFAULT: 4): ')
        if depthStr != '':
            deepest_depth = int(deepest_depth)

        print('\n1: User 2: AI (Just press Enter to exit game)')

        init_fill_center_board()
        while True:

            for p in range(2):

                print_board()

                player = str(p + 1)
                print('PLAYER: ' + player)

                if is_terminal_node(board, player):
                    if p == 0:
                        other_player = '2'
                    else:
                        other_player = '1'

                    if is_terminal_node(board, other_player):
                        print()
                        print_board()
                        print('Player cannot play! Game ended!')
                        print('Score User: ' + str(eval_board(board, '1')))
                        print('Score AI  : ' + str(eval_board(board, '2')))
                        sys.exit()
                    else:
                        print('No moves, Player ' + player + 'skipped')
                        continue

                elif player == '1':  # 1st AI's turn
                    x_move_to, y_move_to = best_move(board, player, cpu_mode1, deepest_depth)

                    if (x_move_to, y_move_to) != (-1, -1):
                        board, total_piece_taken = execute_move(board, x_move_to, y_move_to, player)
                        print('1st AI played (X Y): ' + str(x_move_to) + ' ' + str(y_move_to))
                        print('# of pieces taken: ' + str(total_piece_taken))

                else:  # 2nd AI's turn
                    x_move_to, y_move_to = best_move(board, player, cpu_mode2, deepest_depth)

                    if (x_move_to, y_move_to) != (-1, -1):
                        board, total_piece_taken = execute_move(board, x_move_to, y_move_to, player)
                        print('2nd AI played (X Y): ' + str(x_move_to) + ' ' + str(y_move_to))
                        print('# of pieces taken: ' + str(total_piece_taken))
    else:
        print('Invalid input!')
