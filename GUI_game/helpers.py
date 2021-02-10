from GUI_game.canvas import tk


def clean_screen():
    for el in tk.grid_slaves():
        el.destroy()


def matrix():
    matrix = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    return  matrix