from tkinter import Button, Entry, Label
from GUI_game.canvas import tk
from GUI_game.helpers import clean_screen, matrix


def get_row_winner(board):
    for row in range(len(board)):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return True
    return False


def get_column_winner(board):
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return True
    return False


def get_diagonal_winner(board):
    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[2][0] == board[1][1] == board[0][2] != '':
        return True
    return False


def check_winner(board):
    row_winner = get_row_winner(board)
    column_winner = get_column_winner(board)
    diagonal_winner = get_diagonal_winner(board)
    return row_winner or column_winner or diagonal_winner


def button_1(board, sign):
    row=0
    col=0
    board[row][col]=sign
    Button('1').destroy()
    Label(text=sign).grid(row=3, column=3)


def play(p1, p2, p1_s, p2_s):
    clean_screen()
    board = matrix()
    print("Player one starts first")
    while not check_winner(board):
        for i in range(1,3):
            if i%2==0:
                sign=p2_s
                name=p2
            else:
                sign = p1_s
                name = p1
            Button(tk, text="1", font='Arial 40', width=3, bg="yellow", fg="red",
                   command=lambda: button_1(board, sign)).grid(row=3, column=3, padx=20, pady=20)
            Button(tk, text="2", font='Arial 40', width=3, bg="yellow", fg="red").grid(row=3, column=4)
            Button(tk, text="3", font='Arial 40', width=3, bg="yellow", fg="red").grid(row=3, column=5)
            Button(tk, text="4", font='Arial 40', width=3, bg="yellow", fg="red").grid(row=4, column=3)
            Button(tk, text="5", font='Arial 40', width=3, bg="yellow", fg="red").grid(row=4, column=4)
            Button(tk, text="6", font='Arial 40', width=3, bg="yellow", fg="red").grid(row=4, column=5)
            Button(tk, text="7", font='Arial 40', width=3, bg="yellow", fg="red").grid(row=5, column=3)
            Button(tk, text="8", font='Arial 40', width=3, bg="yellow", fg="red").grid(row=5, column=4)
            Button(tk, text="9", font='Arial 40', width=3, bg="yellow", fg="red").grid(row=5, column=5, padx=20,
                                                                                       pady=20)


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
