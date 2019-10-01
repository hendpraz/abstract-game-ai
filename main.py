import sys
import os
import tkinter
import time

from engine import best_move
from board import init_board, print_board, execute_move, is_legal_move, board, eval_board, is_terminal_node, board_size

m = tkinter.Tk()
m.title("Othello AI")
frame = tkinter.Frame(m)
frame.pack()
X = tkinter.IntVar()
Y = tkinter.IntVar()
X.set(-1)
Y.set(-1)

def setXY(r,c):
    global X
    global Y
    X.set(r)
    Y.set(c)

#buttons = [[int(0) in range(board_size)] in range(board_size)]
buttons = []
for i in range(board_size):
    temp = []
    for j in range(board_size):
        temp.append(tkinter.Button(frame,width=3,command=lambda k=i,l=j: setXY(l,k)))
        temp[j].grid(row = i, column = j)
    buttons.append(temp)

def render(board):
    global buttons
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] != '0':
                buttons[i][j]["text"] = board[i][j]

buttons[3][3]["text"] = '2'
buttons[4][4]["text"] = '2'
buttons[4][3]["text"] = '1'
buttons[3][4]["text"] = '1'

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

        print('\n1: User 2: AI (Just press Enter to exit game)')

        init_board()
        while True:

            player = ''
            for p in range(2):

                print_board()

                player = str(p + 1)
                print('PLAYER: ' + player)

                if is_terminal_node(board, player):
                    print('Player cannot play! Game ended!')
                    print('Score User: ' + str(eval_board(board, '1')))
                    print('Score AI  : ' + str(eval_board(board, '2')))
                    sys.exit()

                if player == '1':  # user's turn
                    while True:
                        X.set(-1)
                        frame.wait_variable(X)
                        x_move_to = X.get()
                        y_move_to = Y.get()
                        # x_move_to, y_move_to = map(int, input('X Y: ').split())

                        if is_legal_move(board, x_move_to, y_move_to, player):
                            board, total_piece_taken = execute_move(board, x_move_to, y_move_to, player)
                            render(board)
                            print('# of pieces taken: ' + str(total_piece_taken))
                            m.update()
                            break
                        else:
                            print('Your move: ' + str(x_move_to) + ' ' + str(y_move_to) + ' is invalid move! Try again!')

                else:  # AI's turn
                    x_move_to, y_move_to = best_move(board, player, cpu_mode, deepest_depth)
                    buttons[y_move_to][x_move_to]["text"] = '2'
                    if (x_move_to, y_move_to) != (-1, -1):
                        board, total_piece_taken = execute_move(board, x_move_to, y_move_to, player)
                        render(board)
                        m.update()
                        print('AI played (X Y): ' + str(x_move_to) + ' ' + str(y_move_to))
                        print('# of pieces taken: ' + str(total_piece_taken))

m.mainloop()
