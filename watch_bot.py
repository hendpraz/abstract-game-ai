from board import init_board, print_board, execute_move, board, eval_board, is_terminal_node
from engine import best_move
import sys

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

        init_board()
        while True:

            for p in range(2):

                print_board()

                player = str(p + 1)
                print('PLAYER: ' + player)

                if is_terminal_node(board, player):
                    print('Players cannot play! Game ended!')
                    print('Score 1st AI : ' + str(eval_board(board, '1')))
                    print('Score 2nd AI  : ' + str(eval_board(board, '2')))
                    sys.exit()

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
