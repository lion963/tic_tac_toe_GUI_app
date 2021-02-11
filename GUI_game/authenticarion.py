from tkinter import *
from tkinter.ttk import *
from tkinter import Button, Entry, Label
from GUI_game.canvas import tk
from GUI_game.helpers import clean_screen, matrix


def get_row_winner(board):
    for row in range(len(board)):
        if board[row][0] == board[row][1] == board[row][2]:
            return True
    return False


def get_column_winner(board):
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col]:
            return True
    return False


def get_diagonal_winner(board):
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[2][0] == board[1][1] == board[0][2]:
        return True
    return False


def check_winner(board):
    row_winner = get_row_winner(board)
    column_winner = get_column_winner(board)
    diagonal_winner = get_diagonal_winner(board)
    if any([row_winner, column_winner, diagonal_winner]):
        return True
    return False


def button(btn1, board, x, y, k, l):
    board[x][y]=sign
    btn1.destroy()
    Label(text=sign, font='Arial 40', width=3).grid(row=k, column=l)



def render_main_screen():
    Label(text="Enter player 1 name:").grid(row=1, column=1)
    Label(text="Enter player 1 sign:").grid(row=2, column=1)
    player_1_name = Entry(tk)
    player_1_sign = Entry(tk)
    player_1_name.grid(row=1, column=2)
    player_1_sign.grid(row=2, column=2)
    Label(text="Enter player 2 name:").grid(row=3, column=1)
    Label(text="Enter player 2 sign:").grid(row=4, column=1)
    player_2_name = Entry(tk)
    player_2_sign = Entry(tk)
    player_2_name.grid(row=3, column=2)
    player_2_sign.grid(row=4, column=2)
    Button(tk, text="Enter", bg="green", fg="white",
           command=lambda: play(player_1_name.get(), player_2_name.get(), player_1_sign.get(),
                                player_2_sign.get())).grid(row=5, column=2)


def play(p1, p2, p1_s, p2_s):
    global sign, name
    sign=p1_s
    name=p1
    clean_screen()
    board = matrix()
    print("Player one starts first")
    btn1=Button(tk, text="1", font='Arial 40', width=3, bg="yellow", fg="red", command=lambda: button(btn1, board,0, 0, 3, 3))
    btn1.grid(row=3, column=3)
    btn2=Button(tk, text="2", font='Arial 40', width=3, bg="yellow", fg="red", command=lambda: button(btn2, board, 0, 1, 3, 4))
    btn2.grid(row=3, column=4)
    btn3=Button(tk, text="3", font='Arial 40', width=3, bg="yellow", fg="red", command=lambda: button(btn3, board, 0, 2, 3, 5))
    btn3.grid(row=3, column=5)
    btn4=Button(tk, text="4", font='Arial 40', width=3, bg="yellow", fg="red", command=lambda: button(btn4, board, 1, 0, 4, 3))
    btn4.grid(row=4, column=3)
    btn5=Button(tk, text="5", font='Arial 40', width=3, bg="yellow", fg="red", command=lambda: button(btn5, board, 1, 1, 4, 4))
    btn5.grid(row=4, column=4)
    btn6=Button(tk, text="6", font='Arial 40', width=3, bg="yellow", fg="red", command=lambda: button(btn6, board, 1, 2, 4, 5))
    btn6.grid(row=4, column=5)
    btn7=Button(tk, text="7", font='Arial 40', width=3, bg="yellow", fg="red", command=lambda: button(btn7, board, 2, 0, 5, 3))
    btn7.grid(row=5, column=3)
    btn8=Button(tk, text="8", font='Arial 40', width=3, bg="yellow", fg="red", command=lambda: button(btn8, board, 2, 1, 5, 4))
    btn8.grid(row=5, column=4)
    btn9=Button(tk, text="9", font='Arial 40', width=3, bg="yellow", fg="red", command=lambda: button(btn9, board, 2, 2, 5, 5))
    btn9.grid(row=5, column=5)
    Label(text=f'{name} choose a cell:',font='Arial 13', fg="green").grid(row=0, column=0)
    # while not check_winner(board):
    #     for i in range(1,3):
    #         if i%2==0:
    #             sign=p2_s
    #             name=p2
    #         else:
    #             sign = p1_s
    #             name = p1



