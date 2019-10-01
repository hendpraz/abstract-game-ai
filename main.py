import sys
import tkinter

from board_checking import is_legal_move, is_terminal_node
from board_identity import board_size, board
from board_io import print_board
from board_operation import init_fill_center_board, execute_move, eval_board
from engine import best_move

m = tkinter.Tk()
m.title("Othello AI")
menu = tkinter.Menu(m)
m.config(menu=menu)
menu.add_command(label='New Game')
bottom_text = tkinter.Frame(m)
bottom_text.pack(side='bottom')
header_text = tkinter.Frame(m)
header_text.pack()
frame = tkinter.Frame(m)
frame.pack()
X = tkinter.IntVar()
Y = tkinter.IntVar()
gui_cpu_mode = tkinter.IntVar()
gui_cpu_mode.set(-1)
X.set(-1)
Y.set(-1)

config = tkinter.Toplevel(m)
config.title("Config")
config.attributes("-topmost", True)
cpu_mode_frame = tkinter.Frame(config)
cpu_mode_frame.pack(side='left')
deep_frame = tkinter.Frame(config)
deep_frame.pack(side='right')
button_frame = tkinter.Frame(config)
button_frame.pack(side='bottom')
tkinter.Label(cpu_mode_frame, text="select cpu mode").pack()
tkinter.Radiobutton(cpu_mode_frame, text='Minimax', variable=gui_cpu_mode, value=1).pack(anchor='w')
tkinter.Radiobutton(cpu_mode_frame, text='Minimax w/ Alpha-Beta Pruning', variable=gui_cpu_mode, value=2).pack(
    anchor='w')
tkinter.Radiobutton(cpu_mode_frame, text='Random Bot', variable=gui_cpu_mode, value=3).pack(anchor='w')
tkinter.Label(deep_frame, text="select difficulty (depth level)").pack()
spin_box = tkinter.Spinbox(deep_frame, from_=1, to=10)
spin_box.pack(anchor='e')
deepest_depth = -1


def set_depth(s):
    global config
    global deepest_depth
    deepest_depth = int(s.get())
    config.destroy()


ok_button = tkinter.Button(button_frame, text="OK", command=lambda: set_depth(spin_box))
ok_button.pack(anchor='s', side='bottom')
frame.wait_window(config)


def set_xy(r, c):
    global X
    global Y
    X.set(r)
    Y.set(c)


header = tkinter.Label(header_text, height=2, width=30, text="")
header.pack()

buttons = []
for i in range(board_size):
    temp = []
    for j in range(board_size):
        temp.append(tkinter.Button(frame, width=3, command=lambda k=i, l=j: set_xy(l, k)))
        temp[j].grid(row=i, column=j)
    buttons.append(temp)

text = tkinter.Label(bottom_text, height=4, width=30, text="")
text.pack()


def render(current_board):
    global buttons
    for i in range(board_size):
        for j in range(board_size):
            if current_board[i][j] != '0':
                buttons[i][j]["text"] = current_board[i][j]


buttons[3][3]["text"] = '2'
buttons[4][4]["text"] = '2'
buttons[4][3]["text"] = '1'
buttons[3][4]["text"] = '1'

if __name__ == '__main__':
    cpu_mode = int(gui_cpu_mode.get())
    if 0 < cpu_mode < 4:
        print(cpu_mode)
        print(deepest_depth)

        print('\n1: User 2: AI (Just press Enter to exit game)')

        init_fill_center_board()
        while True:

            player = ''
            for p in range(2):

                print_board()

                player = str(p + 1)
                print('PLAYER: ' + player)
                print('Score User: ' + str(eval_board(board, '1')))
                print('Score AI  : ' + str(eval_board(board, '2')))
                text['text'] = 'PLAYER: ' + player + "\n"
                text['text'] += 'Score User: ' + str(eval_board(board, '1')) + "\n"
                text['text'] += 'Score AI  : ' + str(eval_board(board, '2')) + "\n"
                m.update()

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
                        text['text'] = 'Player cannot play! Game ended!'
                        text['text'] += 'Score User: ' + str(eval_board(board, '1'))
                        text['text'] += 'Score AI  : ' + str(eval_board(board, '2'))
                        sys.exit()
                    else:
                        print('No moves, Player ' + player + 'skipped')
                        text['text'] = 'No moves, Player ' + player + 'skipped'
                        continue

                if player == '1':  # user's turn
                    while True:
                        X.set(-1)
                        frame.wait_variable(X)
                        x_move_to = X.get()
                        y_move_to = Y.get()

                        legal, message = is_legal_move(board, x_move_to, y_move_to, player)
                        if legal:
                            board, total_piece_taken = execute_move(board, x_move_to, y_move_to, player)
                            render(board)
                            print('# of pieces taken: ' + str(total_piece_taken))
                            text['text'] += '# of pieces taken: ' + str(total_piece_taken)
                            m.update()
                            break
                        else:
                            print(message)
                            print(
                                'Your move: ' + str(x_move_to) + ' ' + str(y_move_to) + ' is invalid move! Try again!')
                            text['text'] += 'Your move: ' + str(x_move_to) + ' ' + str(
                                y_move_to) + ' is invalid move! Try again!'

                else:  # AI's turn
                    x_move_to, y_move_to = best_move(board, player, cpu_mode, deepest_depth)
                    buttons[y_move_to][x_move_to]["text"] = '2'
                    if (x_move_to, y_move_to) != (-1, -1):
                        board, total_piece_taken = execute_move(board, x_move_to, y_move_to, player)
                        render(board)
                        m.update()
                        print('AI played (X Y): ' + str(x_move_to) + ' ' + str(y_move_to))
                        print('# of pieces taken: ' + str(total_piece_taken))
                        header['text'] = 'AI played (X Y): ' + str(x_move_to) + ' ' + str(y_move_to) + '\n'
                        header['text'] += '# of pieces taken: ' + str(total_piece_taken)

m.mainloop()
